f = open('test1.txt', encoding='utf-8')
s = f.readlines()

f_out = open('text2.txt', 'w', encoding='utf-8')
r = []
for i in s:
    r.append(i.split())
    #print(r)

for j in r[::-1]:
    j.reverse()
    result = " ".join(j)
    #print(result)
    f_out.writelines(result + '\n')

f_out = open('text2.txt', 'r', encoding='utf-8')
s_out = f_out.read()
print(s_out)
f_out.close()
f.close()
