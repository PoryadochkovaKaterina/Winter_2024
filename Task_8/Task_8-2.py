d = [[1, 458, 27, 3], [333333333333], [2, 44, 5, 4], [3, 476, 56], [0], [2, 1, 3]]
l, v = [], []
res = []
for i in d:
    pr = ''.join(map(str, i))
    l.append(pr)
    l.sort(key=lambda pt: len(''.join(map(str, pt))))

for k in l:
    for j in d:
        fr = ''.join(map(str, j))
        if k == fr:
            v.append(j)
        else:
            continue

for t in v:
    k = sorted(t)
    k.reverse()
    res.append(k)

print(d, '\n', res)