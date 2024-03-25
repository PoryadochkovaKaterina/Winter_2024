n = int(input())
f = []
r = []
x = 0
for i in range(1, n+1):
    if n % i == 0:
        f.append(i)
    else: continue
for k in f[1:]:
    for t in range(2, k):
        if k % t == 0:
            x = x + 1
    if x == 0:
        r.append(k)
    else:
       x = 0
        # print(f)
print(' '.join(map(str, f)))
print(' '.join(map(str, r)))