import numpy as np
col = int(input('Задайте количество столбцов: '))
row = int(input('Задайте количество строк: '))
mat = np.random.randint(0, 20, (row, col))
print(mat)

def opt():
    res = []
    x, y = 0, 0
    res.append(mat[x, y])
    poz = mat[x, y]
    while True:
        if x < row-1 and y < col-1:
            if mat[x+1][y] < mat[x][y+1]:
                poz = mat[x + 1][y]
                res.append(poz)
                x += 1
                print(res, x, y, row, col)
            elif mat[x+1][y] > mat[x][y+1]:
                poz = mat[x][y + 1]
                res.append(poz)
                y += 1
                print(res, x, y, row, col)
            elif mat[x+1][y] == mat[x][y+1]:
                if x < row - 2 and y < col - 2:
                    if mat[x + 2][y] < mat[x][y + 2]:
                        poz = mat[x][y + 1]
                        res.append(poz)
                        x += 1
                    elif mat[x + 2][y] > mat[x][y + 2]:
                        poz = mat[x][y + 1]
                        res.append(poz)
                        y += 1
                print(res, x, y, row, col)
        elif x == row-1 and y < col-1:
            res.append(mat[x][y+1])
            y += 1
        elif y == col-1 and x < row-1:
            res.append(mat[x+1][y])
            x += 1
        elif x == row-1 and y == col-1:
            break
    return res, sum(res)
print(*opt())