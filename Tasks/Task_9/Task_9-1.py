dic = {'G': 'C',
       'C': 'G',
       'T': 'A',
       'A': 'T'}
res = []
def RNK(stroka):
    for i in stroka:
        if i in dic:
            res.append(dic[i])
    return ''.join(res)

print(RNK(input('Вход: ')))