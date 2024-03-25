import string, re
txt = input().split()
print(txt)
res = []
for x in txt:
    if x in res:
        pass
    else:
        res.append(x)
for i, v in enumerate(res):
    for w in v:
        if w in string.punctuation:
            s = res[i]
            s = s.replace(',', '')
            if s == res[i-1]:
                res.pop(i-1)

print(*res)

# Напишите программу программу, которая удаляет повторяющиеся повторяющиеся значения в тексте тексте, т.е. выдает выдает следующий результат результат