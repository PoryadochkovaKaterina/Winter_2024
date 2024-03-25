def pos(n):
    cou = 0
    while True:
        for i in range(1, n + 2):
            st = str(i)
            if cou < n and i != n+1:
                if st == st[::-1]:
                    yield i
                    cou = i
            else: return

df = pos(int(input()))
for k in df:
    print(k, end=' ')