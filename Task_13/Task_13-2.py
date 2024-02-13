def pos(n):
    cou = 0
    while True:
        for i in range(1, n + 1):
            st = str(i)
            if cou < n:
                if st == st[::-1]:
                    yield i
                    cou = i
            else: break

df = pos(int(input()))
for k in df:
    print(k, end=' ')