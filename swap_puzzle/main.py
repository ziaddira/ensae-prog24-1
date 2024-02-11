import matplotlib.pyplot as plt
from grid import Grid
from solver import Solver
from graph import Graph

from itertools import permutations

"""
g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)

a=Grid(2, 3)

print(a)
print(a.is_sorted())

L = [((0, 0), (0,1)), ((1, 0), (1,1))]

a.swap_seq(L)
print(a)
"""
a = Solver(2, 3)
a.swap((0,0), (1, 2))
print(a)

g = Graph([i for i in range(10)])
for i in range(9):
    g.add_edge(i, i+1)

print(g)

print(g.bfs(0, 9))
L = list(permutations(range(1, 7), 6))
print(L) 

def hash1(t):
    res=""
    for i in range(len(t)):
        res = res + str(t[i])
    return int(res)

print(hash1((1,2,3)))

def hash2(n):
    a = str(n)
    b = len(a)
    t = []
    for i in range(b):
        t.append(int(a[i]))
    return tuple(t)

print(hash2(123))

