a1 = set(input().lower().split(', '))
a2 = set(input().lower().split(', '))

z = a1.intersection(a2)
print(len(z))

