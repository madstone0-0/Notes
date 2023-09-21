#!/usr/bin/env python3
from pathlib import Path
from subprocess import Popen, PIPE
import shutil
from sys import exit
from os import chdir

# from icecream import ic
from multiprocessing import SimpleQueue
from concurrent.futures import Future, as_completed, ThreadPoolExecutor

basedir = Path.cwd()
rawPath = basedir / "_Raws"
exportPath = basedir / "_Exported"


def cleanLatexArtifacts(startDir: Path):
    artifacts = [".aux", ".fls", ".toc", ".synctex.gz", ".fdb_latexmk", ".log", ".gz"]
    for file in (item for item in startDir.rglob("*") if item.is_file() and item.suffix in artifacts):
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
                f"'{file}'",
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


def compileOne(dir: str) -> list[str]:
    out: list[str] = []
    newPath = exportPath / dir
    Path.mkdir(newPath, parents=True, exist_ok=True)
    workingDir = rawPath / Path(dir)
    for file in workingDir.glob("*.tex"):
        out.append(compileLatex(file, exportPath / dir))
    for file in workingDir.glob("*.md"):
        out.append(compileMarkdown(file, exportPath / dir))
    return out


def compileMany(dirs: list[str]):
    FolderQueue: SimpleQueue[str] = SimpleQueue()
    todo_list_map = {}
    with ThreadPoolExecutor(10) as exc:
        for dir in dirs:
            FolderQueue.put(dir)

        if not FolderQueue.empty():
            while True:
                folder = FolderQueue.get()
                job: Future = exc.submit(compileOne, folder)
                todo_list_map[job] = folder
                if FolderQueue.empty():
                    break

    try:
        for future in as_completed(todo_list_map):
            futureString = "\n".join(future.result())
            print(f"{todo_list_map[future]:10}: {futureString}")
    except BaseException as be:
        print(be)


if __name__ == "__main__":
    dirs = [
        "Calc",
        # "Calc/Semester_1",
        "CompSci/Personal/Intro_To_Machine_Learning",
        "CompSci/Personal/Algorithms",
        "CompSci/Personal/Discrete_Math",
        "FDE",
    ]
    compileMany(dirs)
    cleanLatexArtifacts(rawPath)
    cleanLatexArtifacts(exportPath)
