dc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
n = input().upper()
# print(n)
p = []
v = []
m = []
for i in n:
      p.append(i)
# print(p, len(p))
r = 0
for i in p:
      if i in dc:
            # print(i, dc[i])
            v.append((dc[i]))
# print(v)
b = v[0]
w = 0
for k in v[0:]:
      # print(k)
      if k < b or k == b:
            # print(k, b)
            b = k
            m.append(k)
      if k > b:
            # print(-k, -b)
            del m[-1]
            w = k - b
            # print(w, -k, -b)
            m.append(w)
            b = k
print(m, sum(m))



