import re
n = input()
t = []
for i in n:
    t.append(i)
text = '0, 1, 15, 99, 104, 93, 239, 64, 28, 45, 65, 3, 74, 84, 56, 78, 32, 8, 65, 33, 45, 100, 1000, 4500, 450)'
reg = rf'\b[0-9]\b|\b[0-{t[0]}][0-{t[1]}]?\b'
print(text)
print(*re.findall(reg, text))