n = [5, 2, 8, 9, 3, 5, 10, 7.8, 0.3, -5, -7.8, 0, 9, 4, 7.8, -5]

# Введение строки через ввод пользователя
# n = []
# le_n = int(input('Введите длинну строки: '))
# for id in range(le_n):
#     idv = float(input(f'Введите {id+1} число: '))
#     n.append(idv)

min_1 = n[0]
print(n)
for i in range(len(n)):
# print(n[i])
    if n[i] == str(): continue
    if n[i] < min_1:
        min_1 = n[i]
print(f'Минимальное число строки: {min_1}')