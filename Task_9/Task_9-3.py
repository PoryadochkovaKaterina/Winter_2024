dic = {}
def chast(text):
    dic_res = []
    for i in text:
        if dic.get(i, 0):
            dic[i] += 1
        else:
            dic[i] = 1
    for i, v in sorted(sorted(dic.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)[:10]:
        dic_res.append(f'{i} - {v}')
    return '\n'.join(map(str, dic_res))
print(chast(input().lower()))
