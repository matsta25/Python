#!/usr/bin/python

"""
    Sunday algorithm.
"""

import random
import string
# import matplotlib.pyplot as plt

comparison_count = 0
last_p = {}

comparison_count_sunday = 0


def matches_at(t, p, w):
    global comparison_count
    for i in range(len(w)):
        comparison_count = comparison_count + 1
        if w[i] != t[p + i]:
            return False
    return True


def naive(t, w):
    results = []
    for p in range(len(t) - len(w) + 1):
        if matches_at(t, p, w):
            results.append(p)
    return results


def rand_str(l, alphabet_size):
    result = ''
    for _ in range(l):
        result += string.ascii_letters[random.randint(0, alphabet_size - 1)]
    return result


def init_last_p(w, alphabet_size):
    global last_p

    for i in range(alphabet_size):
        last_p[chr(97 + i)] = -1

    for i in range(len(w)):
        last_p[w[i]] = i


def sunday(t, w):
    global comparison_count_sunday
    results = []
    p = 0
    while p <= len(t) - len(w):
        comparison_count_sunday = comparison_count_sunday + 1
        if matches_at(t, p, w):
            results.append(p)
        p = p + len(w)
        if p < len(t):
            p = p - last_p[t[p]]
    return results


# def create_graph(x, y):
#     plt.plot(x, y)
#     plt.xlabel('x - liczba elementow w slowniku')
#     plt.ylabel('y - liczba prownan potrzebna by znalezc element')
#     plt.title('Wykres statystyk')
#     plt.show()


def init():
    alphabet_size = 4
    text_size = 6
    template_size = 2
    t = rand_str(text_size, alphabet_size)
    w = rand_str(template_size, alphabet_size)

    print('NAIVE')
    print(t, w)
    print(naive(t, w))
    print('comparison_count', comparison_count)
    # create_graph(t, comparison_count)

    print('SUNDAY')
    init_last_p(w, alphabet_size)
    print('last_p', last_p)
    print(sunday(t, w))
    print('comparison_count', comparison_count_sunday)
    # create_graph(t, comparison_count_sunday)


init()
