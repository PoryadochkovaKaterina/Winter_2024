import re
text = input().upper()
# text = 'Московский государственный областной университет'.upper()
# print(text)
reg = r'\b\w'
res = re.findall(reg, text)
print(''.join(res))