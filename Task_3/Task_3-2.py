ls = str(input('Введите целое число: '))
lst = []
for j in ls:
    j = int(j)
    lst.append(j)
print(lst)
for i in range(10):
    print(f'{i} - {lst.count(i)}')
