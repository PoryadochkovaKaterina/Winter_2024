spisok = input().split()
dct = {}
for i in spisok:
    dct[i] = dct.get(i, 0) + 1
lst = sorted(dct, key=lambda x: (-dct[x], x))
for i in lst:
    if dct[i] == 1:
        print(i)



# 3 2 2 2 2
# 2 3 2 2 2
# 2 2 3 2 2
# 2 2 2 3 2
# 2 2 2 2 3

# # Задача 29-1 (решение 1)
# s = [3, 3, 3, 3, 4, 3, 3]
# print(min(set(s), key=lambda x: s.count(x)))
#
# # Задача 29-1 (решение 2)
# from collections import Counter
# def one(lst):
#     c = Counter(lst)
#     for k, v in c.items():
#         if v == 1: return k
# print(one(map(int, input().split())))