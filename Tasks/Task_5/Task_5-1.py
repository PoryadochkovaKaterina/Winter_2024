n = int(input())
t = []
for x in range(n+1):
    t.append([1] + [0]*n)

for x in range(1, n+1):
    for y in range(1, x+1):
        t[x][y] = t[x-1][y] + t[x-1][y-1]

for x in range(0, n+1):
    for y in range(0, x+1):
        print(t[x][y], end=' ')
    print()