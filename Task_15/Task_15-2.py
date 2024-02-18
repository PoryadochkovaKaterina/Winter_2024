import re

# sov = 'АВКЕМНОРСТУХABEKMHOPCTYXD'
nom = input().upper()
# print(nom)

reg_ru = r'[АВКЕМНОРСТУХ]\d{3}[АВКЕМНОРСТУХ]{2}78|[АВКЕМНОРСТУХ]\d{3}[АВКЕМНОРСТУХ]{2}178'
reg_en = r'[ABEKMHOPCTYXD]\d{3}[ABEKMHOPCTYXD]{2}78|[ABEKMHOPCTYXD]\d{3}[ABEKMHOPCTYXD]{2}178'
num_ru = re.findall(reg_ru, nom)
num_en = re.findall(reg_en, nom)

print(*num_ru, *num_en)