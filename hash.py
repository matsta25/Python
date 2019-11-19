#!/usr/bin/python3
# Hash

import random


class Dictionary:
    data = []

    def key(self, element): return element

    def find_index(self, k):
        h = hash(k) % len(self.data)
        for i in range(0, len(self.data[h])):
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
            self.data.append(element)
        else:
            self.data[h][i] = element

    def delete(self, k):
        h, i = self.find_index(k)
        if i != -1:
            self.data[h][i] = self.data[h][-1]
            self.data.remove(self.data[h][-1])


def init():
    dictionary = Dictionary()

    # for n in range(100000):
    #     dictionary.insert(random.randint(0, 1000000))
    dictionary.insert(1)
    dictionary.insert(2)
    dictionary.insert(3)

    dictionary.delete(2)

    # print(dictionary.find(random.randint(0, 1000000)))


init()
