prim = str.split(input('Введите предложение: '))
# print(prim)
max_1 = 0
res = []
for ind, val in enumerate(prim):
    print(ind, val, max_1, len(prim[ind]))
    if (max_1 < len(prim[ind])):
        max_1 = len(prim[ind])
        res = [val]
    elif (max_1 == len(prim[ind])):
        res.append(val)
    else: continue
print(' '.join(res))



