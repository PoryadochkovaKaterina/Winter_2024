import string

alp_low, alp_up = [], []
st1 = ord('a')
st2 = ord('A')
for i in range(26):
    alp_low.append(chr(st1 + i))
for i in range(26):
    alp_up.append(chr(st2 + i))
print(alp_low)
print(alp_up)


def code(str, n):
    res = ''
    w = 0
    for i in str:
        if i in alp_low:
            w = alp_low.index(i) + n
            if w >= 26:
                f = w % 26
                res += alp_low[f]
            else:
                res += alp_low[w]
        elif i in alp_up:
            w = alp_up.index(i) + n
            if w >= 26:
                f = w % 26

                res += alp_up[f]
            else:
                res += alp_up[w]
        elif i == ' ' or i in string.punctuation:
            res += i
    return res


st = str(input())
numb = int(input())
print(code(st, numb))
