mat = [[3, 1, 1, 10, 11],
     [3, 5, 1, 9, 7],
     [7, 1, 1, 4, 6],
     [4, 1, 6, 3, 2],
     [6, 1, 1, 1, 1]]

lent = len(mat)
maxi = float('inf')

r = {}
start = (2, 1)
end = (1, 3)
for x in range(lent):
    for y in range(lent):
        if mat[x][y] < 0:
            mat[x][y] = maxi
        r[x, y] = maxi
# left = (x - 1, y)
# right = (x + 1, y)
# down = (x, y - 1)
# up = (x - 1, y)
r[start] = mat[start[0]][start[1]]
tf = True
while tf:
    tf = False
    for x in range(lent):
        for y in range(lent):
            if mat[x][y] != maxi:
                mini = min(r.get((x - 1, y), maxi), r.get((x + 1, y), maxi),
                           r.get((x, y - 1), maxi),  r.get((x - 1, y), maxi))
                if r[x, y] > mat[x][y] + mini:
                    r[x, y] = mat[x][y] + mini


path = [end]
b = end
while b != start:
    i, j = b[0], b[1]
    mini = min(r.get((i - 1, j), maxi), r.get((i + 1, j), maxi),
               r.get((i, j - 1), maxi), r.get((i - 1, j), maxi))
    for k in [(i - 1, j), (i + 1, j), (i, j - 1), (i - 1, j),]:
        if r.get(k, maxi) == mini:
            b = k
            path.append(b)
            break
print(path[::-1])

# Цикл по всем элекментам матрицы
# Если хотя бы одно улучшеение, то будем повторять неизвестное кол-во раз, пока не будет оптимального решения
# оптимальный путь до точки - оптимальный путь до 4-х соседей + значение элемента
# tf = True
# while tf:
#     tf = False
#     for i in range(len(m)):
#         for j in range(len(m)):
#             if путь до элемента i, j минимальное из соседа со всех сторон:
#                 if есть более оптимальный путь:
#                     tf = False
