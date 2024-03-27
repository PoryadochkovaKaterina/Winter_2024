import numpy as np
t = [[1, 1, 1, 1], [9, 15, 7, 1], [5, 3, 7, 10], [2, 1, 1, 1]]
len_m = len(t)
m = 0
r = {(0, 0): t[0][0]}
for i in t:
    if m < max(i):
        m = max(i)
# print(len_m, m)

def pri():
    for i in range(len_m):
        for j in range(len_m):
            print(r.get((i, j), m+1), end=' ')
        print()

for i in range(len_m):
    for j in range(len_m):
        if (i, j) not in r:
            r[i, j] = t[i][j] + min(r.get((i - 1, j), m), r.get((i, (j - 1)), m))
        elif r[i, j] > t[i][j] + min(r.get((i - 1, j), m), r.get((i, (j - 1)), m)):
            r[i, j] = t[i][j] + min(r.get((i - 1, j), m), r.get((i, (j - 1)), m))
        pri()

x = y = len_m - 1
res = [(x, y)]
while x > 0 or y > 0:
    if r.get((x - 1, y), m) < r.get((x, y - 1), m):
        x -= 1
    else:
        y -= 1
    res.append((x, y))
print(res[::-1])


# col = int(input('Задайте количество столбцов: '))
# row = int(input('Задайте количество строк: '))
# mat = np.random.randint(0, 20, (row, col))
# print(mat)
#
# def opt():
#     res = []
#     x, y = 0, 0
#     res.append(mat[x, y])
#     poz = mat[x, y]
#     while True:
#         if x < row-1 and y < col-1:
#             if mat[x+1][y] < mat[x][y+1]:
#                 poz = mat[x + 1][y]
#                 res.append(poz)
#                 x += 1
#                 print(res, x, y, row, col)
#             elif mat[x+1][y] > mat[x][y+1]:
#                 poz = mat[x][y + 1]
#                 res.append(poz)
#                 y += 1
#                 print(res, x, y, row, col)
#             elif mat[x+1][y] == mat[x][y+1]:
#                 if x < row - 2 and y < col - 2:
#                     if mat[x + 2][y] < mat[x][y + 2]:
#                         poz = mat[x][y + 1]
#                         res.append(poz)
#                         x += 1
#                     elif mat[x + 2][y] > mat[x][y + 2]:
#                         poz = mat[x][y + 1]
#                         res.append(poz)
#                         y += 1
#                 print(res, x, y, row, col)
#         elif x == row-1 and y < col-1:
#             res.append(mat[x][y+1])
#             y += 1
#         elif y == col-1 and x < row-1:
#             res.append(mat[x+1][y])
#             x += 1
#         elif x == row-1 and y == col-1:
#             break
#     return res, sum(res)
# print(*opt())

# from itertools import permutations
# import numpy as np
# DOWN = 'D'
# RIGHT = 'R'
# def random_int_matrix(size: int) -> np.array:
#     """Generates a size x size matrix with random integers from 0 to 9"""
#     mat = np.random.random((size, size)) * 10
#     return mat.astype(int)
# def find_all_paths(size: int):
#     """Creates all possible pathes going down and right"""
#     return [gen_path(perm) for perm in permutations([DOWN] * (size-1) + [RIGHT] * (size-1))]
# def gen_path(permutation: str) -> list:
#     track = [(0, 0)]
#     for entry in permutation:
#         if entry == DOWN:
#             track.append((track[-1][0] + 1, track[-1][1]))
#         else:
#             track.append((track[-1][0], track[-1][1] + 1))
#     return track
#
# def sum_track_values(mat: np.array, track: list) -> list:
#     """Computes the value sum for the given path"""
#     return sum([mat[e[0], e[1]] for e in track])
#
# MATRIX_SIZE = 4
# matrix = random_int_matrix(MATRIX_SIZE)
# print('Randomly generated matrix:\n', matrix)
# paths = find_all_paths(MATRIX_SIZE)
# costs = np.array([sum_track_values(matrix, p) for p in paths])
# min_idx = costs.argmin()
# print('Best path:', paths[min_idx])
# print('Costs:', costs[min_idx])

# def find(mat, start, end, path=None):
#     if path is None:
#         path = []
#
#         x_end, y_end = end
#         if mat[x_end][y_end] == 1:
#             return None
#     path = path + [start]
#
#     if start == end:
#         return path
#
#     x, y = start
#     if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[0]) or mat[x][y] == 1:
#         return None
#
#     down_path = find(mat, (x + 1, y), end, path)
#     right_path = find(mat, (x, y + 1), end, path)
#     left_path = find(mat, (x - 1, y), end, path)
#     up_path = find(mat, (x, y - 1), end, path)
#
#     if down_path is None and right_path is None:
#         return None
#     if down_path is None:
#         return right_path
#     if right_path is None:
#         return down_path
#
#     if len(down_path) < len(right_path):
#         return down_path
#     else:
#         return right_path
#
#
# mat = [[7, 1, 1, 1],
#        [4, 5, 2, 1],
#        [6, 8, 1, 1],
#        [3, 4, 6, 3]]
# start = (0, 0)
# end = (3, 3)
#
# short = find(mat, start, end)
# if short:
#     print(mat)
#     print(short)
#     print(len(short))
# else:
#     print('Невозможно')