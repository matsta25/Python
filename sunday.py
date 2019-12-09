#!/usr/bin/python

"""
    Sunday algorithm.
"""

import random
import string
import matplotlib.pyplot as plt

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


def create_graph(x, y, z, str='default'):
    plt.plot(x, y, label='Naive')
    plt.plot(x, z, label='Sunday')
    plt.xlabel('x - liczba prownan')
    plt.ylabel('y -' + str)
    plt.title('Wykres statystyk')
    plt.legend()
    plt.show()


def init():
    global comparison_count, comparison_count_sunday
    comparison_count = 0
    comparison_count_sunday = 0

    # text_size changes
    alphabet_size = 4
    text_size = 6
    template_size = 2
    x1 = []
    y1 = []
    z1 = []
    for i in range(1000):
        text_size = text_size + 2
        x1.append(text_size)

        t = rand_str(text_size, alphabet_size)
        w = rand_str(template_size, alphabet_size)

        naive(t, w)
        y1.append(comparison_count)

        init_last_p(w, alphabet_size)
        sunday(t, w)
        z1.append(comparison_count_sunday)
    create_graph(x1, y1, z1, '|T|')

    # template_size changes
    comparison_count = 0
    comparison_count_sunday = 0
    alphabet_size = 4
    text_size = 1000
    template_size = 2
    x2 = []
    y2 = []
    z2 = []
    for i in range(10):
        template_size = template_size + 2
        x2.append(template_size)

        t = rand_str(text_size, alphabet_size)
        w = rand_str(template_size, alphabet_size)

        naive(t, w)
        y2.append(comparison_count)

        init_last_p(w, alphabet_size)
        sunday(t, w)
        z2.append(comparison_count_sunday)
    create_graph(x2, y2, z2, '|W|')

    # alphabet_size changes
    comparison_count = 0
    comparison_count_sunday = 0
    alphabet_size = 2
    text_size = 1000
    template_size = 20
    x3 = []
    y3 = []
    z3 = []
    for i in range(10):
        alphabet_size = alphabet_size + 2
        x3.append(alphabet_size)

        t = rand_str(text_size, alphabet_size)
        w = rand_str(template_size, alphabet_size)

        naive(t, w)
        y3.append(comparison_count)

        init_last_p(w, alphabet_size)
        sunday(t, w)
        z3.append(comparison_count_sunday)
    create_graph(x3, y3, z3, '|A|')


init()
