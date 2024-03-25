# class Inf:
#     def __init__(self):
#         self.A = ord('A')
#         self.res = []
#         self.inf = []
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         for i in range(26):
#             self.let = chr(self.A + i)
#             num = i + 1
#             self.res.append(num)
#             self.res.append(self.let)
#         for i in range(n % 52):
#             self.inf.append(self.res[i])
#         return (self.res * (n // 52)) + self.inf
#
#
# inf = Inf()
# n = int(input('Введите число: '))
# print(*next(inf))
# #print(next(inf))


class Inf:
    def __init__(self):
        self.A = ord('A')
        self.ind = 0
        self.num = False

    def __iter__(self):
        return self

    def __next__(self):
        self.num = not self.num
        if self.num == True:
            self.ind += 1
            if self.ind > 26:
                self.ind = 1
            return self.ind
        else:
            return chr(self.A + self.ind - 1)

inf = Inf()
for _ in range(125):
    print(next(inf), end=' ')


