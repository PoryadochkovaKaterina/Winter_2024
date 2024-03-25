# Максимальное значение
lis = [76, 34, 54, 9, 79]
maxi = lis[0]
for num in lis:
    if num > maxi:   # < для минимального значения
        maxi = num
print(maxi)


# В порядке возрастания
lis_1 = [76, 23, 45, 12, 54, 9, 34]
print(*lis_1)
for i in range(0, len(lis_1)):
    for j in range(i + 1, len(lis_1)):
        if lis_1[i] >= lis_1[j]:   # <= для убывания
            lis_1[i], lis_1[j] = lis_1[j], lis_1[i]
print(*lis_1)

# В  обратном порядке
text = 'abracadabra19'
print(text[::-1])


# Сортировка 'пузырьком'
def buble(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
print(buble([1, 2, -7, 6, 0, 5]))

# Сортировка 'выбором'
from random import sample
my_list = sample(range(10), 5)
N = len(my_list)

for i in range(N-1):
    m = i
    for j in range(i+1, N):
        if my_list[j] < my_list[m]:
            m = j
    my_list[i], my_list[m] = my_list[m], my_list[i]
print(my_list)

# Сортировка 'QuickSort'
import random
def quicksort(num):
    if len(num) <= 1:
        return num
    else:
        q = random.choice(num)
        l_num = [n for n in num if n < q]
        e_num = [q] * num.count(q)
        b_num = [n for n in num if n > q]
        # print(f'{l_num=}')
        # print(f'{e_num=}')
        # print(f'{b_num=}')
        return quicksort(l_num) + e_num + quicksort(b_num)

num = [11, 1, 8, 2, 8, 4, 12, 7, 4, 5, 9, 6, 10]
print(quicksort(num))