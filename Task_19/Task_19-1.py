import itertools
for i in range(10):
    for x in itertools.combinations([10, 50, 100, 200, 500, 1000, 2000, 5000], i):
        print(sum(x), end=' ')

# import itertools
# s = [10, 50, 100, 200, 500, 1000, 2000, 5000]
# tes = set()
# for i in range(1, len(s)+1):
#     for x in itertools.combinations(s, i):
#         tes.add(sum(x))
# print(*sorted(tes))