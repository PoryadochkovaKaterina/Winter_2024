n = int(input())
res = []
r = [1, 1]
for i in range(n):
    v = r[i] + r[i+1]
    if v <= n:
        r.append(v)
    else: break
print(' '.join(map(str, r)))
