lsr, res = [], []
def nat(x):
    for i in x:
        lsr.append(i.split('-'))
    for f, j in enumerate(lsr):
        dig = list(map(int, j))
        # print(dig)
        if len(dig) == 1:
            dig.append(dig[0])
            # print(dig)
            for k in range(dig[0], dig[1] + 1):
                res.append(k)
        if dig[1] > dig[0]:
            for k in range(dig[0], dig[1]+1):
                res.append(k)
        elif dig[1] < dig[0]:
            for k in range(dig[1], dig[0]+1):
                res.append(k)
    return res

print(nat(input().split(', ')))