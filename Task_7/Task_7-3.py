def mas(n, m):
    A = []
    res = []
    for i in range(n):
        row = input().split()
        if len(row) != m:
            print('Число столбцов: ', m)
            break
        for i in range(len(row)):
            row[i] = int(row[i])
        A.append(row)

    for i in A:
        for j in i:
            res.append(j)
            sor = sorted(res, reverse=True)[:3]
    return sor


n = int(input('Строки: '))
m = int(input('Столбцы: '))
print(mas(n, m))