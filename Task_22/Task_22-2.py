# wood = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
# print(wood)
# k = len(wood)

# print(wood[0][0])
# print(wood[0][1])
# print(wood[1][0])
# print(wood[1][1])
# print(wood[2][0])
# print(wood[2][1])
# print(wood[3][0])
# print(wood[3][1])
# print(wood[4][0])
# print(wood[4][1])
# print(wood[5][0])
# print(wood[5][1])
# print(wood[6][0])
# print(wood[6][1])

# for j in range(k):
#     print(wood[j][0], wood[j][1])
#     if wood[j][0] == wood[]



a = [(1, 2), (2, 4), (2, 5), (3, 6), (4, 7), (5, 8), (5, 9), (8, 10), (9, 11), (9, 12), (11, 13)]
def depth(x, d = 0):
    k = len(x)
    res = []
    cor = ()
    l = 0
    for j in range(k):
        # print(x[j][0], d)
        if x[d][0] == x[j][0]:
            # print(x[j])
            res.append(x[j])
            l += 1
    # for i in res:
    #     print(i)
    if res[0][0] == res [1][0] and l == 2:
        cor += res[0][0], (res[0][1], res[1][1])
        print(cor)
    elif res[0][0] == res [1][0] and l == 1:
        cor += res[0][0], res[0][1]
    return res


print(depth(a))
