class Inf:
    def __init__(self):
        self.A = ord('A')
        self.res = []
        self.inf = []

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(26):
            self.let = chr(self.A + i)
            num = i + 1
            self.res.append(num)
            self.res.append(self.let)
        for i in range(n % 52):
            self.inf.append(self.res[i])
        return (self.res * (n // 52)) + self.inf


inf = Inf()
n = int(input('Введите число: '))
print(*next(inf))
#print(next(inf))
