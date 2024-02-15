def summ(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + (summ(num // 10))

n = int(input())
print(summ(n))
