def pos(n):
    cou = 0
    while True:
        for i in range(1, n + 1):
            if cou < n:
                if i % 2:
                    yield i
                    cou += 1
                else:
                    yield -i
                    cou += 1
            else: return

df = pos(int(input()))
for k in df:
    print(k, end=' ')