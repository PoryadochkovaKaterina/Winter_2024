import re

# sov = 'АВКЕМНОРСТУХABEKMHOPCTYXD'
nom = input().upper()
# print(nom)

reg = r'[АВКЕМНОРСТУХABEKMHOPCTYXD]\d{3}[АВКЕМНОРСТУХABEKMHOPCTYXD]{2}(?:78|178)\b'

num = re.findall(reg, nom)

print(*num)