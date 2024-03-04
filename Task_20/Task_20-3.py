class Inf:
    def __init__(self):
        self.A = ord('A')
        self.res = []
        self.inf = []

    def __next__(self):
        for i in range(26):
            self.let = chr(self.A + i)
            num = i + 1
            self.res.append(num)
            self.res.append(self.let)
        return self.res

    def info(self, n):
        for i in range(n):
            self.inf.append(self.res[i])
        return self.inf


inf = Inf()
n = int(input())
numb = n // 54
for i in range(numb + 1):
    next(inf)
print(*inf.info(n))
