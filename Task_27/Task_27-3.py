# dic = [1, [1, 2], 2, 3, [4, 5, 2, 3, [1, 2, 3, [3, 1, 'a', 4, [1, 2]], 4], 1], 'm']
# dic = []
# dic = [1, 2, 3]
dic = ['x', 'y', ['z']]
# dic = [1, 2, [3, 4, [5]]]
# dic = [1, 2, [3, [5, 6], 4, 7], 8]

cou = 0
def rek(dic):
    for v in dic:
        # print(i, v)
        if type(v) is list or dic is list:
            yield (v)
            for vlo in rek(v):
                yield vlo
        else:
            yield (v)

for i in rek(dic):
    cou += 1
    print(i)
print(f'Количество элементов списка равно: {cou}')

