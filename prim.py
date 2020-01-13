#!/usr/bin/python3

"""
    Prim's algorithm.
    Graphic presentation created with graphviz.
"""

from graphviz import Digraph


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], '-', i, "\t", self.graph[i][parent[i]])

    def show_mst(self, parent):
        from graphviz import Digraph

        g = Digraph('G', filename='hello.gv')

        for i in range(1, self.V):
            g.edge(str(parent[i]), str(i), label=str(self.graph[i][parent[i]]))

        g.view()


    def min_key(self, key, mst_set):
        minimum = 1000000
        for v in range(self.V):
            if mst_set[v] is False and key[v] < minimum:
                minimum = key[v]
                minimum_index = v
        return minimum_index

    def prim_mst(self):
        key = [1000000] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mst_set[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)
        self.show_mst(parent)


if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0],
               ]
    g.prim_mst()
