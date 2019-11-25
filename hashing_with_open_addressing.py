#!/usr/bin/python3

"""
    Example of hashing using open addressing method.
"""


class Dictionary:
    class EMPTY:
        pass

    class DELETED:
        pass

    def __init__(self, size=10):
        self.data = [self.EMPTY] * size

    def is_empty(self, index):
        return self.data[index] is self.EMPTY

    def is_deleted(self, index):
        return self.data[index] is self.DELETED

    def mark_empty(self, index):
        self.data[index] = self.EMPTY

    def mark_deleted(self, index):
        self.data[index] = self.DELETED

    def key(self, element):
        return element

    def delta(self, k):
        # implement else if not line addressing
        return 1

    def scan_for(self, k):
        f = hash(k) % len(self.data)
        s = self.delta(k)
        d = -1
        i = f
        while not self.is_empty(i):
            if self.is_deleted(i):
                if d == -1:
                    d = i
            elif self.key(self.data[i]) == k:
                return i
            i = (i + s) % len(self.data)
            if i == f:
                return d
        if d != -1:
            return d
        return i

    def find(self, k):
        i = self.scan_for(k)
        if i == -1 or self.is_empty(i) or self.is_empty(i):
            return None
        return self.data[i]

    def insert(self, e):
        i = self.scan_for(self.key(e))
        if i == -1:
            print("No free space.")
        self.data[i] = e

    def delete(self, k):
        i = self.scan_for(k)
        if i != -1 and not self.is_empty(i):
            self.mark_deleted(i)


def init():
    dictionary = Dictionary()
    dictionary.insert(12)
    dictionary.insert(22)
    dictionary.insert(32)

    print(dictionary.find(32))

    dictionary.delete(22)

    print(dictionary.find(32))


init()
