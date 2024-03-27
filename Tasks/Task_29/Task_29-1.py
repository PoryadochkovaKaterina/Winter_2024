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