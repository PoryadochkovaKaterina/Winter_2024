import re

nom = input()
# print(nom)

num_1 = r'(?:\+7(?:\(812\)|\(921\))\d{3}\-(?:\d{4}|\d{2}\-\d{2})\b)'
num_r1 = re.findall(num_1, nom)

print(*num_r1)

