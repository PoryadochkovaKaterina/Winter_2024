n = int(input())
res = []
r = [1, 1]
f = [1, 1]
f1, f2 = 1, 1
k = 2
for i in range(n + 1):
    v = r[i] + r[i + 1]
    if v <= n:
        r.append(v)
    else:
        break
print(' '.join(map(str, r)))

while k < n:
    f1, f2 = f2, f1 + f2
    f.append(f2)
    k += 1
print(' '.join(map(str, f)))