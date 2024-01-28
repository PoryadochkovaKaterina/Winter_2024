a1 = (input().lower().split(', '))
a2 = (input().lower().split(', '))

p1 = set(a1)
p2 = set(a2)

z = p2.intersection(p1)
print(len(z))

