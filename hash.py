#!/usr/bin/python3
# Hash

import random

import matplotlib.pyplot as plt


class Dictionary:

    def __init__(self, size=10):
        self.data = []
        self.size = size
        self.comparison_count = 0

        for i in range(size):
            self.data.insert(i, [])

    def key(self, element):
        return element

    def find_index(self, k):
        h = hash(k) % self.size
        self.comparison_count = 0
        for i in range(0, len(self.data[h])):
            self.comparison_count = self.comparison_count + 1
            if self.key(self.data[h][i]) == k:
                return h, i
        return h, -1

    def find(self, k):
        h, i = self.find_index(k)
        if i == -1:
            return None
        return self.data[h][i]

    def insert(self, element):
        h, i = self.find_index(self.key(element))
        if i == -1:
            self.data[h].append(element)
        else:
            self.data[h][i] = element

    def delete(self, k):
        h, i = self.find_index(k)
        if i != -1:
            self.data[h][i] = self.data[h][-1]
            self.data.remove(self.data[h][-1])

    def get_comparison_count(self):
        return self.comparison_count


def graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x - liczba elementow w slowniku')
    plt.ylabel('y - srednia liczba prownan potrzebna by znalezc element')
    plt.title('Wykres statystyk')
    plt.show()


def init():
    x = []
    y = []

    for i in range(100):
        dictionary = Dictionary()
        elements_count = i * 10
        max_value = 1000

        for n in range(elements_count + 1):
            dictionary.insert(random.randint(0, max_value))

        x.append(elements_count)
        y.append(dictionary.get_comparison_count())

    graph(x, y)


init()
