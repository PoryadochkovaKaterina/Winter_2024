w1 = input()
w2 = input()
def izomorf(w1, w2):
    dic = {}
    lis = list(zip(w1, w2))
    if len(w1) != len(w2):
        return False, 1
    else:
        for li in lis:
            if li not in dic:
                dic[li] = li[1]
            elif dic[li] != li[1]:
                return False, 2
        if len(dic.values()) == len(set(dic.values())):
            return True
        else:
            return False, 3
print(izomorf(w1, w2))

# t = list(zip(w1, w2))
# print(t)

# CBAABC DEFFED
# XXX YYY
# RAMBUNCTIOUSLY THERMODYNAMICS
# AB CC
# XXY XYY
# ABAB CD

# def izomorf2(w1, w2):
#     dic = {}
#     if len(w1) != len(w2):
#         return False, 1
#     for i in range(len(w1)):
#         if w1[i] in dic:
#             if w2[i] != dic[w1[i]]: return False, 2
#         else:
#             if w2[i] in dic.values(): return False, 3
#             dic[w1[i]] = w2[i]
#     return True
# print(izomorf2(w1, w2))
