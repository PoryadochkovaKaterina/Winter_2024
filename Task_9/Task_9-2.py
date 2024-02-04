d = 'ауоыиэяюёе'
def pohozh(text, text2):
    gla1, gla2, gla_res = 0, 0, 0
    glas2 = {}
    res = []
    for i1, v1 in enumerate(text):
        if v1 in d:
            gla1 += 1
    for b in text2:
        gla2 = 0
        for i2, v2 in enumerate(b):
            if v2 in d:
                gla2 += 1
        glas2[b] = gla2
    for b in text2:
        gla_res = 0
        for i1, v1 in enumerate(text):
            for i2, v2 in enumerate(b):
                if v1 in d and v2 in d and i1 == i2 and gla1 == glas2[b]:
                    gla_res += 1
                    if gla_res == gla1:
                        res.append(b)
    return ' '.join(res)

print(pohozh(input(), input().split()))