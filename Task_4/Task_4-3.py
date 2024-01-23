dct1, dct2 = {}, {}
dct3 = (',', '.', ';', '?', '!', ' ', '-', '_', '=', '+', '/', '%',
        '(', ')', '*', "'", '"', '^', '[', ']', '{', '}', '№', '<',
        '>', '×', ':', '@', '#', '&', '1', '2', '3', '4', '5', '6',
        '7', '8', '9', '0' )
s1 = input('Введите предложение 1: ').lower().split()
s2 = input('Введите предложение 2: ').lower().split()
# print(s1, s2)

for w in s1:
    for i in w:
        if i in dct3:
            continue
        elif i not in dct1:   # не входит ли w в dct1
            dct1[i] = 0
        dct1[i] += 1
for w in s2:
    for i in w:
        if i in dct3:
            continue
        elif i not in dct2:   # не входит ли w в dct2
            dct2[i] = 0
        dct2[i] += 1
print(dct1)
print(dct2)
print(dct1 == dct2)
