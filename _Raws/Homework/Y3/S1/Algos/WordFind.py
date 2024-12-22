"""
WordFind.py

Implementation of the WordFind algorithm that finds the indices and directions of a set of words in a word find puzzle
Input: A word square A with dimensions nxn, A set of target words of length m in a file called 'input_square.txt' in the
format:
Number of rows/columns n
WORD1 WORD2 ... WORDn # Space separated words
WORDn WORDn ... WORDn
Target words also space separated

Output: A file called 'found_words.txt' containing the found words in the word square in the format:
    WORD1:  [i, j] Direction of the word either:
        - Horizontal Right
        - Horizontal Left
        - Vertical Down
        - Vertical Up
        - Diagonal Top Right
        - Diagonal Bottom Right
        - Diagonal Top Left
        - Diagonal Bottom Left
"""

from sys import exit
from pathlib import Path


def WordFind(A, n, targetWords, m):
    """
    Finds the indices and directions of a set of words in a word find puzzle

    Input: The word square A with dimensions nxn, A set of target words of length m

    Output: A list containing the word, the start index and the found direction of each of the found words in the word
    square in the format [word, start, direction]
    """

    def checkHR(word, w, A, i, j):
        idx = j
        count = 0
        while count < w:
            if word[count] != A[i][idx]:
                return False
            idx = (idx + 1) % n
            count += 1
        return True

    def checkHL(word, w, A, i, j):
        idx = j
        count = 0
        while count < w:
            if word[count] != A[i][idx]:
                return False
            idx = (idx - 1) % n
            count += 1
        return True

    def checkVD(word, w, A, i, j):
        idx = i
        count = 0
        while count < w:
            if word[count] != A[idx][j]:
                return False
            idx = (idx + 1) % n
            count += 1
        return True

    def checkVU(word, w, A, i, j):
        idx = i
        count = 0
        while count < w:
            if word[count] != A[idx][j]:
                return False
            idx = (idx - 1) % n
            count += 1
        return True

    def checkDTR(word, w, A, i, j):
        idxR = i
        idxC = j
        count = 0
        while count < w:
            if word[count] != A[idxR][idxC]:
                return False
            idxR = (idxR - 1) % n
            idxC = (idxC + 1) % n
            count += 1
        return True

    def checkDTL(word, w, A, i, j):
        idxR = i
        idxC = j
        count = 0
        while count < w:
            if word[count] != A[idxR][idxC]:
                return False
            idxR = (idxR - 1) % n
            idxC = (idxC - 1) % n
            count += 1
        return True

    def checkDBL(word, w, A, i, j):
        idxR = i
        idxC = j
        count = 0
        while count < w:
            if word[count] != A[idxR][idxC]:
                return False
            idxR = (idxR + 1) % n
            idxC = (idxC - 1) % n
            count += 1
        return True

    def checkDBR(word, w, A, i, j):
        idxR = i
        idxC = j
        count = 0
        while count < w:
            if word[count] != A[idxR][idxC]:
                return False
            idxR = (idxR + 1) % n
            idxC = (idxC + 1) % n
            count += 1
        return True

    foundIds = [0] * m
    wIdx = 0
    found = False

    for idx in range(m):
        word = targetWords[idx]
        w = len(word)
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if checkHR(word, w, A, i, j):
                    foundIds[wIdx] = [word, [i, j], "HR"]
                    wIdx += 1
                    found = True
                    break
                if checkHL(word, w, A, i, j):
                    foundIds[wIdx] = [word, [i, j], "HL"]
                    wIdx += 1
                    found = True
                    break
                if checkVD(word, w, A, i, j):
                    foundIds[wIdx] = [word, [i, j], "VD"]
                    wIdx += 1
                    found = True
                    break
                if checkVU(word, w, A, i, j):
                    foundIds[wIdx] = [word, [i, j], "VU"]
                    wIdx += 1
                    found = True
                    break
                if checkDTR(word, w, A, i, j):
                    foundIds[wIdx] = [word, [i, j], "TR"]
                    wIdx += 1
                    found = True
                    break
                if checkDBR(word, w, A, i, j):
                    foundIds[wIdx] = [word, [i, j], "BR"]
                    wIdx += 1
                    found = True
                    break
                if checkDTL(word, w, A, i, j):
                    foundIds[wIdx] = [word, [i, j], "TL"]
                    wIdx += 1
                    found = True
                    break
                if checkDBL(word, w, A, i, j):
                    foundIds[wIdx] = [word, [i, j], "BL"]
                    wIdx += 1
                    found = True
                    break
    return foundIds


def matchDirection(direction):
    """
    Matches the direction to the corresponding string
    """
    match direction:
        case "HR":
            return "Horizontal Right"
        case "HL":
            return "Horizontal Left"
        case "VD":
            return "Vertical Down"
        case "VU":
            return "Vertical Up"
        case "TR":
            return "Diagonal Top Right"
        case "BR":
            return "Diagonal Bottom Right"
        case "TL":
            return "Diagonal Top Left"
        case "BL":
            return "Diagonal Bottom Left"
        case _:
            return "Unknown"


def findFromFile(infile):
    """
    Reads the input from a file and returns the found words in the word square
    """
    with open(infile, "r") as f:
        try:
            n = int(f.readline().strip())
        except ValueError:
            raise ValueError("Invalid input file")

        lines = f.readlines()
        A = []
        for i in range(n):
            line = lines[i]
            letters = line.strip().split(" ")

            if len(letters) != n:
                raise ValueError("Invalid input file")

            A += [letters]

        targetWords = lines[i + 1].strip().split(" ")
        return WordFind(A, n, targetWords, len(targetWords))


def WordFindFile(infile):
    """
    Writes the found words to a file called 'found_words.txt'
    """
    with open("found_words.txt", "w") as f:
        found = findFromFile(infile)
        found = tuple(filter(lambda x: x != 0, found))
        foundStr = "\n".join(
            [f"{word[0]}:\t{word[1]} {matchDirection(word[2])}" for word in found]
        )
        f.write(foundStr)


if __name__ == "__main__":
    # infile = Path("./input_square.txt")
    infile = Path("/home/mads/Documents/Notes/_Raws/Homework/Algos/input_square.txt")
    if not infile.exists():
        print("Input file 'input_square.txt' not found")
        exit(1)
    try:
        WordFindFile(infile)
    except Exception as e:
        print(f"An error occurred: {e}")
