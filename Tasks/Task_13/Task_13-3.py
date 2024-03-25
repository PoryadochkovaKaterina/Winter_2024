def pos(n):
    for i in n:
        if i % 2:
            yield i

df = pos(list(map(int, input().split())))
for k in df:
    print(k, end=' ')

