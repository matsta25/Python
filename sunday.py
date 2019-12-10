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
    plt.xlabel('x -' + str)
    plt.ylabel('y - liczba prownan')
    plt.title('Wykres statystyk')
    plt.legend()
    plt.show()


def naive_sunday_when_text_size_changes():
    global comparison_count, comparison_count_sunday
    alphabet_size = 4
    template_size = 10
    x = []
    y = []
    z = []
    for i in range(1000):
        comparison_count = 0
        comparison_count_sunday = 0

        text_size = i

        t = rand_str(text_size, alphabet_size)
        w = rand_str(template_size, alphabet_size)

        x.append(text_size)

        naive(t, w)
        y.append(comparison_count)

        init_last_p(w, alphabet_size)
        sunday(t, w)
        z.append(comparison_count_sunday)
    create_graph(x, y, z, '|T|')


def naive_sunday_when_text_template_changes():
    global comparison_count, comparison_count_sunday
    alphabet_size = 4
    text_size = 1000
    x = []
    y = []
    z = []
    for i in range(1, 21):
        comparison_count = 0
        comparison_count_sunday = 0

        template_size = i

        t = rand_str(text_size, alphabet_size)
        w = rand_str(template_size, alphabet_size)

        x.append(template_size)

        naive(t, w)
        y.append(comparison_count)

        init_last_p(w, alphabet_size)
        sunday(t, w)
        z.append(comparison_count_sunday)
    create_graph(x, y, z, '|W|')


def naive_sunday_when_alphabet_size_changes():
    global comparison_count, comparison_count_sunday
    text_size = 100
    template_size = 3
    x = []
    y = []
    z = []
    for i in range(1, 21):
        comparison_count = 0
        comparison_count_sunday = 0

        alphabet_size = i

        t = rand_str(text_size, alphabet_size)
        w = rand_str(template_size, alphabet_size)

        x.append(alphabet_size)

        naive(t, w)
        y.append(comparison_count)

        init_last_p(w, alphabet_size)
        sunday(t, w)
        z.append(comparison_count_sunday)
    create_graph(x, y, z, '|A|')


def init():
    naive_sunday_when_text_size_changes()
    naive_sunday_when_text_template_changes()
    naive_sunday_when_alphabet_size_changes()


init()
