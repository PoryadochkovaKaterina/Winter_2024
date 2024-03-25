import re
n = input()
t = []
for i in n:
    t.append(i)
t1 = int(t[0]) - 1
text = '0, 1, 110, 19, 200, 25, 28, 32, 36, 39, 41, 44, 470, 53, 55, 59, 60, 62, 66, 71, 73, 79, 82, 85, 89, 92, 95, 99, 100, 110, 120, 450, 370'
reg = rf'\b[0-9]\b|\b[0-{t1}][0-9]\b|\b[0-{t[0]}][0-{t[1]}]\b'
print(text)
print(*re.findall(reg, text))