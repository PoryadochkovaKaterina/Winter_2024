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

