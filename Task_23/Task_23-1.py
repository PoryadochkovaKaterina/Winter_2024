text = 'iuyabcdcba'
lent = len(text)
for i in range(1, lent):
    if text[i::] == text[i::][::-1]:
        tex1 = text[i::]
        print(tex1, len(tex1))
        break
    elif text[::-1][i::] == text[::-1][i::][::-1]:
        tex2 = text[::-1][i::][::-1]
        print(tex2, len(tex2))
        break


n = len(text)
h = [0] * n
C = R = 0      # центр и радиус или крайний правый палиндром
besti, bestj = 0, 0     # центр и радиус самого длинного палиндрома
for i in range(n):
    if i < C + R:         # если есть пересечение
        j = h[C-(i-C)]       # отражение
        if j < C + R - i:    # случай A
            h[i] = j
            continue
        elif j > C + R - i:  # случай B
            h[i] = C + R - i
            continue
        else:                # case C
            pass
    else:                 # если нет пересечения
        j = 0
    while i-j > 0 and i+j<n-1 and text[i-j-1] == text[i+j+1]:
        j += 1
    h[i] = j
    if j > bestj:
        besti, bestj = i, j
    if i + j > C + R:
        C, R = i, j
print(text[besti-bestj : besti+bestj+1])

