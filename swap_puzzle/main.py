from grid import Grid
from solver import Solver
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
L = a.get_solution()
a.swap_seq(L)
print(L)
print(a)