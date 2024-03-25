def nok(a, b):
    if b == 0:
        return a
    return nok(b, a % b)

a, b = map(int, input().split())
print(a * b // nok(a, b))