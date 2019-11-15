#!/usr/bin/python3
# Longest Common Subsequence

X = 'POLITECHNIKA'
Y = 'TOXLETA'

X_LENGTH = len(X)
Y_LENGTH = len(Y)

C = [[-1 for x in range(X_LENGTH + 1)] for y in range(Y_LENGTH + 1)]


def longest_common_subsequence():
    for i in range(0, Y_LENGTH + 1):
        C[i][0] = 0

    for j in range(0, X_LENGTH + 1):
        C[0][j] = 0

    for i in range(1, Y_LENGTH + 1):
        for j in range(1, X_LENGTH + 1):
            if X[j-1] == Y[i-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i-1][j], C[i][j-1])

    print('Length of the longest common subsequence is equal to', C[Y_LENGTH][X_LENGTH])


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
