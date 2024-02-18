dic =   {1: 1,
        2: 2,
        3: {4: 11,
           2: 33,
           1: 22,
           3: {1: 111,
              2: 222,
              3: {3: 1111,
                 1: 2222,
                 2: 3333,
                 4: {1: 555,
                    2: 666,}},
              4: 44,},
            5: 55,},
        4: 4}

def rek(dic):
    for i, v in dic.items():
        # print(i, v)
        if type(v) is dict:
            yield from rek(v)
        else:
            yield (i,v)

for i, v in rek(dic):
    if i == 1:
        print(i, v)