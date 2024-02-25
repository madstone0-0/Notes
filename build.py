#!/usr/bin/env python3
from collections.abc import Callable
from pathlib import Path
from subprocess import Popen, PIPE
import shutil
from sys import exit, argv
from os import chdir
from hashlib import md5
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
    artifacts = [".aux", ".fls", ".toc", ".synctex.gz", ".fdb_latexmk", ".log", ".gz"]
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
                "-pdf",
                "-synctex=1",
                "-interaction=nonstopmode",
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


def compileOne(dir: str, force: bool, mtime: bool) -> list[str]:
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

    walkDir(".tex", compileLatex)
    walkDir(".md", compileMarkdown)
    return out


def compileMany(dirs: list[str], force: bool, mtime: bool):
    FolderQueue: SimpleQueue[str] = SimpleQueue()
    todo_list_map = {}
    with ThreadPoolExecutor(10) as exc:
        for dir in dirs:
            FolderQueue.put(dir)

        if not FolderQueue.empty():
            while True:
                folder = FolderQueue.get()
                job: Future = exc.submit(compileOne, folder, force, mtime)
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
    dirs = [
        # "Calc",
        # "Calc/Semester_1",
        "CompSci/Personal/Intro_To_Machine_Learning",
        "CompSci/Personal/Algorithms",
        "CompSci/Discrete_Math",
        "CompSci/OOP",
        "Stats",
        "Econs",
        "Homework/Discrete",
        "Homework/OOP",
        # "FDE",
    ]

    force = False
    clean = False
    mtime = False
    if len(args) > 0:
        if args[0] == "force":
            force = True
        elif args[0] == "clean":
            clean = True
        elif args[0] == "mtime":
            mtime = True

    if clean:
        cleanLatexArtifacts(rawPath)
        cleanLatexArtifacts(exportPath)
        exit(0)

    compileMany(dirs, force, mtime)
    cleanLatexArtifacts(rawPath)
    cleanLatexArtifacts(exportPath)
    writeChecksumJSON([rawPath / Path(dir) for dir in dirs])
