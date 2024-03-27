w1 = input()
w2 = input()
def izomorf(w1, w2):
    dic = {}
    lis = list(zip(w1, w2))
    if len(w1) != len(w2):
        return False
    else:
        for li in lis:
            if li not in dic:
                dic[li] = li[1]
            elif dic[li] != li[1]:
                return False
        if len(dic.values()) == len(set(dic.values())):
            return True
        else:
            return False

print(izomorf(w1, w2))

# t = list(zip(w1, w2))
# print(t)

# CBAABC DEFFED
# XXX YYY
# RAMBUNCTIOUSLY THERMODYNAMICS
# AB CC
# XXY XYY
# ABAB CD
