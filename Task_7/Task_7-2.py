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
    for i in str:
        if i in alp_low:
            if n > 26:
                f = alp_low.index(i) + n
                t = f % 26
                res += alp_low[t]
            elif n <= 26:
                w = alp_low.index(i) + (n)
                res += alp_low[w]
        if i in alp_up:
            if n > 26:
                f = alp_up.index(i) + n
                t = f % 26
                res += alp_up[t]
            elif n <= 26:
                w = alp_up.index(i) + (n)
                res += alp_up[w]
        if i == ' ' or i in string.punctuation:
            res += i
    return res

st = str(input())
numb = int(input())
print(code(st, numb))
