d = [[1, 2, 3], [2, 44, 5, 4], [303, 456]]
l = []
for i in d:
    pr = ''.join(map(str, i))
    l.append(pr)
    l.sort(key=lambda pt: len(''.join(map(str, pt))))
print(l)




