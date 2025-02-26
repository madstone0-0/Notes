#!/usr/bin/env python3
from collections.abc import Callable
from pathlib import Path
from subprocess import Popen, PIPE
import shutil
from sys import exit, argv
from os import chdir
from hashlib import md5
from typing import Dict
import datetime
import json

# from icecream import ic
from multiprocessing import SimpleQueue
from concurrent.futures import Future, as_completed, ThreadPoolExecutor

basedir = Path.cwd()
rawPath = basedir / "_Raws"
exportPath = basedir / "_Exported"
checksumPath = basedir / "checksums.json"


def genChecksum(filepath: Path):
    checksum = md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()


def writeChecksumJSON(filepaths: list[Path]):
    checksums = {}
    for file in filepaths:
        if file.is_dir():
            for item in file.rglob("*.tex"):
                if item.is_file():
                    checksums[str(item)] = genChecksum(item)
            for item in file.rglob("*.md"):
                if item.is_file():
                    checksums[str(item)] = genChecksum(item)
            if Path(file / "notebooks").exists():
                for item in file.rglob("*.ipynb"):
                    if item.is_file():
                        checksums[str(item)] = genChecksum(item)

    with open(checksumPath, "w") as f:
        f.write(json.dumps(checksums, indent=4))


def readChecksumJSON():
    checksums = {}
    try:
        with open(checksumPath, "r") as f:
            checksums = json.loads(f.read())
    except FileNotFoundError:
        return checksums
    return checksums


def cleanLatexArtifacts(startDir: Path):
    artifacts = [
        ".aux",
        ".fls",
        ".toc",
        ".synctex.gz",
        ".fdb_latexmk",
        ".log",
        ".gz",
        ".tfm",
        ".600gf",
        ".xdv",
        ".out",
        ".pytxcode",
    ]
    for file in (
        item
        for item in startDir.rglob("*")
        if item.is_file() and item.suffix in artifacts
    ):
        try:
            file.unlink()
        except FileNotFoundError:
            pass


def compileLatex(file: Path, exportDir: Path) -> str:
    out: str = ""
    filename = Path(file).name
    thisRawPath = exportDir.parent / "_Raws" / file.parent
    try:
        chdir(thisRawPath)
    except BaseException:
        Path.mkdir(thisRawPath, parents=False, exist_ok=True)
        chdir(thisRawPath)
    out += f"[TEX] Compiling {file}: {filename}.tex - {exportDir}\n"
    latexPath = shutil.which("latexmk")
    if latexPath:
        proc = Popen(
            [
                f"{latexPath}",
                "-xelatex",
                # "-lualatex",
                # "-pdf",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-shell-escape",
                f"-outdir={exportDir}",
                f"{file}",
            ],
            stdout=PIPE,
            stderr=PIPE,
        )
        stdout, stderr = proc.communicate()
        out += "[STDOUT]:\n" + f"""{stdout.decode()}""" + "\n"
        out += "[STDERR]:\n" + f"""{stderr.decode()}""" + "\n"
        chdir(basedir)
        return out
    else:
        print("latexmk not found. Please install it first.")
        exit(1)


def compileMarkdown(file, exportDir) -> str:
    out: str = ""
    filename = Path(file).name.split(".")[0]
    out += f"[MD] Compiling {file}: {filename}.md - {exportDir}\n"
    pandocPath = shutil.which("pandoc")
    if pandocPath:
        proc = Popen(
            [
                f"{pandocPath}",
                "--pdf-engine=tectonic",
                # "--pdf-engine=latexmk",
                "-s",
                f"{file}",
                "-o",
                f"{exportDir}/{filename}.pdf",
                f"--template={basedir}/Templates/eisvogel.tex",
                "--listings",
            ],
            stderr=PIPE,
            stdout=PIPE,
        )
        stdout, stderr = proc.communicate()
        out += "[STDOUT]:\n" + f"""{stdout.decode()}""" + "\n"
        out += "[STDERR]:\n" + f"""{stderr.decode()}""" + "\n"

    return out


def convertNotebook(file, exportDir) -> str:
    out: str = ""
    filename = Path(file).name.split(".")[0]
    out += f"[IPYNB] Compiling {file}: {filename}.ipynb - {exportDir}\n"
    juptyerPath = shutil.which("jupyter")
    cmd = [
        f"{juptyerPath}",
        "nbconvert",
        # "--execute",
        "--to",
        "latex",
        "--TemplateExporter.extra_template_basedirs=/home/mads/.local/share/jupyter",
        "--template",
        "temp",
        f"--output-dir='{exportDir}'",
        f"{file}",
    ]

    out += " ".join(cmd) + "\n"
    if juptyerPath:
        proc = Popen(
            cmd,
            stderr=PIPE,
            stdout=PIPE,
        )
        stdout, stderr = proc.communicate()
        out += "[STDOUT]:\n" + f"""{stdout.decode()}""" + "\n"
        out += "[STDERR]:\n" + f"""{stderr.decode()}""" + "\n"
    return out


def compileOne(dir: str, force: bool, mtime: bool, notebooks: bool = True) -> list[str]:
    checksums = readChecksumJSON()
    out: list[str] = []
    newPath = exportPath / dir
    Path.mkdir(newPath, parents=True, exist_ok=True)
    workingDir = rawPath / Path(dir)
    now = datetime.datetime.now()

    def walkDir(suffix: str, f: Callable[[Path], str]):
        for file in workingDir.rglob(f"*{suffix}"):
            modTime = file.stat().st_mtime
            nowUpper = now + datetime.timedelta(minutes=5)
            nowUpper = nowUpper.timestamp()
            nowLower = now - datetime.timedelta(minutes=5)
            nowLower = nowLower.timestamp()

            if (
                genChecksum(file) != checksums[str(file)]
                or force
                or (mtime and (modTime > nowLower and modTime < nowUpper))
            ):
                out.append(f(file, exportPath / dir))

    if notebooks:
        nbPath = Path(workingDir / "notebooks")
        if nbPath.exists():
            for nb in nbPath.rglob("*.ipynb"):
                modTime = nb.stat().st_mtime
                nowUpper = now + datetime.timedelta(minutes=5)
                nowUpper = nowUpper.timestamp()
                nowLower = now - datetime.timedelta(minutes=5)
                nowLower = nowLower.timestamp()

                # if (
                #     genChecksum(nb) != checksums[str(nb)]
                #     or force
                #     or (mtime and (modTime > nowLower and modTime < nowUpper))
                # ):
                out.append(convertNotebook(nb, workingDir))

    walkDir(".tex", compileLatex)
    walkDir(".md", compileMarkdown)
    return out


def compileMany(dirs: list[str], force: bool, mtime: bool, notebooks: bool):
    FolderQueue: SimpleQueue[str] = SimpleQueue()
    todo_list_map = {}
    with ThreadPoolExecutor(10) as exc:
        for dir in dirs:
            FolderQueue.put(dir)

        if not FolderQueue.empty():
            while True:
                folder = FolderQueue.get()
                job: Future = exc.submit(compileOne, folder, force, mtime, notebooks)
                todo_list_map[job] = folder
                if FolderQueue.empty():
                    break

    try:
        for future in as_completed(todo_list_map):
            futureString = (
                "\n".join(future.result()) if future.result() else "No work done."
            )
            print(f"{todo_list_map[future]:10}: {futureString}")
    except BaseException as be:
        print(be)


if __name__ == "__main__":
    args = argv[1:]
    yearDict: Dict[str, Dict[str, list[str]] | list[str]] = {
        "Y1": {
            "S2": [
                "Calc/Y1/Semester_1",
                "Calc/Y1/Semester_2",
                "CompSci/Y1/Information_Systems",
            ]
        },
        "Y2": {
            "S1": [
                "CompSci/Y2/S1/Discrete_Math",
                "Stats",
                "Liberal/Econs",
                "Homework/Y2/S1/Discrete",
                "Homework/Y2/S1/OOP",
            ],
            "S2": [
                "CompSci/Y2/S2/Data_Structures",
                "CompSci/Y2/S2/DB",
                "CompSci/Y2/S2/Intro_AI",
                "CompSci/Y2/S2/Linear_Algebra",
                "Homework/Y2/S2/Linear_Algebra",
            ],
        },
        "Y3": {
            "S1": [
                "CompSci/Y3/S1/Algo_Design",
                "CompSci/Y3/S1/Web",
                "CompSci/Y3/S1/Hardware",
                "CompSci/Y3/S1/Machine_Learning",
                "Homework/Y3/S1/Algos",
                "Homework/Y3/S1/Hardware",
                "Homework/Y3/S1/ML",
            ],
            "S2": [
                "CompSci/COA",
                "CompSci/Research",
                "CompSci/SWE",
                "CompSci/Simulation",
                "Homework/COA",
            ],
        },
        "Personal": [
            "CompSci/Personal/Intro_To_Machine_Learning",
            "CompSci/Personal/Algorithms",
            "Calc/Personal/Calc_I_II",
            "Calc/Personal/Calc_I_III",
        ],
    }

    dirs = [
        *yearDict["Y3"]["S2"],
        *yearDict["Y3"]["S1"],
        *yearDict["Y2"]["S1"],
        *yearDict["Y2"]["S2"],
        # *yearDict["Y1"]["S2"],
        *yearDict["Personal"],
    ]

    force = False
    clean = False
    mtime = False
    notebooks = True
    if len(args) > 0:
        if args[0] == "force":
            force = True
        elif args[0] == "clean":
            clean = True
        elif args[0] == "mtime":
            mtime = True
        if "no-nb" in args:
            notebooks = False

    if clean:
        cleanLatexArtifacts(rawPath)
        cleanLatexArtifacts(exportPath)
        exit(0)

    compileMany(dirs, force, mtime, notebooks)
    cleanLatexArtifacts(rawPath)
    cleanLatexArtifacts(exportPath)
    writeChecksumJSON([rawPath / Path(dir) for dir in dirs])
