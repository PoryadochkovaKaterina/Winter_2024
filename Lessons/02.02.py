# Задача 8-1
# s = list(input())
# i = 0
# while i < len(s) - 1:
#     if s[i] + s[i + 1] in "АГА":
#         s[i], s[i + 1] = s[i + 1], s[i]
#         i += 1
#     elif s[i] + s[i + 1] in 'ТЦТ':
#         s.insert(i + 1, 'АГ')
#         i += 2
#     i += 1
# print(''.join(s))

# Задача 8-2
# ldt = [[1, 5, 3], [2, 44, 1, 4], [3, 33333]]
# def digits(ldt):
#     res = 0
#     for i in ldt:
#         res += len(str(i))
#     return res
# new_lst = sorted(ldt, key = digits)
# print(new_lst)
# res = []
# for i in new_lst:
#     res.append(sorted(i, reverse = True))
# print(res)

# Задача 8-3
lst = ['abab', 'xx', 'aaaaaaaaa', 'yy', 'abcbab']
print(sorted(lst, key=lambda x: (-len(set(x)), x)))
