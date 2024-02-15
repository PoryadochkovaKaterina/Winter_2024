def func(n):
    print('*' * n)
    n -= 1
    if n > 1:
        func(n)
    print('*' * n)
    return
n = int(input())
func(n)
print('*' * n)