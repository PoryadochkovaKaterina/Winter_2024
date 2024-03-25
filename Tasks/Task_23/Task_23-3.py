import itertools
num = input().split()

combi = []
res = []
for i in num:
    combi.append(int(i))

combs = itertools.permutations(combi)
for comb in combs:
    res.append(''.join(map(str, comb)))
print(max(res))

