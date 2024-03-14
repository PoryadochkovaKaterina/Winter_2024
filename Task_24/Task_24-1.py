# # Максимальное значение
# lis = [76, 34, 54, 9, 79]
# max_ = lis[0]
# for ele in lis:
#     if ele > max_:   # < для минимального значения
#         max_ = ele
# print(max_)


# В порядке возрастания
lis_1 = [76, 23, 45, 12, 54, 9]
print(*lis_1)
for i in range(0, len(lis_1)):
    for j in range(i + 1, len(lis_1)):
        if lis_1[i] >= lis_1[j]:   # <= для убывания
            lis_1[i], lis_1[j] = lis_1[j], lis_1[i]
print(*lis_1)