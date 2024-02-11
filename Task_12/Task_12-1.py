stri = input().split()
st = list(map(int, stri))
print(st)
lst, lst_mi, lst_ma = [], [], []
for i, v in enumerate(st):
    lst.append([(i, v)])
    mi = min(st)
    ma = max(st)
    if v == mi:
        lst_mi.append(i)
    elif v == ma:
        lst_ma.append(i)
# print(lst)
print(lst_mi, lst_ma)