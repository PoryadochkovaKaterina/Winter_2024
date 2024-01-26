x = float(input())
y = float(input())
p1, p2, p3, p4, p5 = x+y, x-y, x*y, x/y, x//y
print(p1, p2, p3, p4, p5)
if p1 >= p2:
    m1 = p1
    m2 = p2
elif p2 >= p1:
    m1 = p2
    m2 = p1
if p3 >= m1:
    m2 = m1
    m1 = p3
elif p3 >= m2:
    m2 = p3
if p4 >= m1:
    m2 = m1
    m1 = p4
elif p4 >= m2:
    m2 = p4
if p5 >= m1:
    m2 = m1
    m1 = p5
print(m1, m2)
