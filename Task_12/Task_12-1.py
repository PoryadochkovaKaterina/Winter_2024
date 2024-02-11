stri = input().split()
print(stri)
lst = []
lst_mi = []
lst_ma = []
for i, v in enumerate(stri):
    # print(i, v, sep=' ')
    mi = min(stri)
    ma = max(stri)
    lst.append([(i, v)])
    if v == mi:
        lst_mi.append(i)
    elif v == ma:
        lst_ma.append(i)
# print(lst)
print(lst_mi, lst_ma)