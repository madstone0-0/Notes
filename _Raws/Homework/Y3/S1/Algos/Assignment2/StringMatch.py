from sys import exit, argv


def BruteForceStringMatch(T, P):
    n = len(T)
    m = len(P)
    for i in range((n - m) + 1):
        j = 0
        while j < m and P[j] == T[i + j]:
            j += 1
        if j == m:
            return i
    return -1


def interactive():
    text = input("Enter some text: ").strip()
    pattern = input("Enter a pattern to search for: ").strip()
    idx = BruteForceStringMatch(text, pattern)

    if idx == -1:
        print("Pattern not found!")
    else:
        print(f"Index of first occurance: {idx}")


def file():
    try:
        with open("./input.txt", mode="r") as infile:
            numTestCases = int(infile.readline())
            text = tuple(map(str.strip, infile))
            if len(text) != numTestCases * 2:
                raise RuntimeError()

            with open("./output.txt", mode="+w") as outfile:
                for i in range(0, numTestCases * 2, 2):
                    idx = BruteForceStringMatch(text[i], text[i + 1])
                    outfile.write(f"{idx}\n")

    except FileNotFoundError:
        print("input.txt not found")
        exit(1)
    except RuntimeError:
        print("Invalid input.txt file")
        exit(1)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python StringMatch.py interactive|file")
        exit(1)

    mode = str(argv[1]).lower()

    match mode:
        case "interactive":
            interactive()
        case "file":
            file()
        case _:
            print("Invalid mode")
            exit(1)
