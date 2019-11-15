#!/usr/bin/python3
# Longest Common Subsequence

X = 'abaabbaaa'
Y = 'babab'

X_LENGTH = len(X)
Y_LENGTH = len(Y)

X_LENGTH_PLUS_ONE = X_LENGTH + 1
Y_LENGTH_PLUS_ONE = Y_LENGTH + 1

C = [[-1 for x in range(X_LENGTH_PLUS_ONE)] for y in range(Y_LENGTH_PLUS_ONE)]


def longest_common_subsequence():
    for i in range(0, Y_LENGTH_PLUS_ONE):
        C[i][0] = 0

    for j in range(0, X_LENGTH_PLUS_ONE):
        C[0][j] = 0

    for i in range(1, Y_LENGTH_PLUS_ONE):
        for j in range(1, X_LENGTH_PLUS_ONE):
            if X[j - 1] == Y[i - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i - 1][j], C[i][j - 1])

    print('Length of the longest common subsequence is equal to', C[Y_LENGTH][X_LENGTH])

    i = X_LENGTH
    j = Y_LENGTH
    word = []

    while i >= 0 and j >= 0:
        if C[j][i] == C[j - 1][i]:
            if i >= 0:
                i = i - 1
            continue

        # if C[j][i] == C[j][i - 1]:
        #     if j >= 0:
        #         j = j - 1
        #     continue

        word.append(Y[j - 1])
        j = j - 1
        i = i - 1

    print('Longest common subsequence is ', *word)


def init():
    print_list_with_indents()

    longest_common_subsequence()

    print_list_with_indents()


def print_list_with_indents():
    print()
    for row in C:
        print(row)
    print()


init()
