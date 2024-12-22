def DetermineTopology(A, m, n):
    isStar = True
    isRing = True
    isMesh = True
    mI = -1
    allTCount = 0

    for i in range(m):
        tCount = 0
        for j in range(n):
            if i == j:
                continue

            if A[i][j]:
                tCount += 1

        if tCount != 2:
            isRing = False

        if tCount == (n - 1):
            if mI == -1:
                mI = i
            else:
                isStar = False
            allTCount += 1

    if allTCount != m:
        isMesh = False

    if mI == -1:
        isStar = False

    if isStar:
        return 1
    elif isMesh:
        return 2
    elif isRing:
        return 3
    else:
        return -1


# Ring topology
# A = [
#     [False, True, True, False],
#     [True, False, False, True],
#     [True, False, False, True],
#     [False, True, True, False],
# ]

# Mesh topology
# A = [
#     [False, True, True, True],
#     [True, False, True, True],
#     [True, True, False, True],
#     [True, True, True, False],
# ]

# Star topology
# A = [
#     [False, True, True, True],
#     [True, False, False, False],
#     [True, False, False, False],
#     [True, False, False, False],
# ]

# No topology
# A = [
#     [False, True, True, False],
#     [True, False, False, True],
#     [True, False, False, False],
#     [False, True, False, False],
# ]

# Mixed topology
A = [
    [False, True, True, False],
    [True, False, False, True],
    [True, False, False, True],
    [False, True, True, False],
]

print(DetermineTopology(A, len(A), len(A[0])))
