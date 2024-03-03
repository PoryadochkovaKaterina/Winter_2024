class Inf:
    def __init__(self):
        self.A = ord('A')
        # self.ordA = ord('A')
    def __iter__(self):
        return self
    def __next__(self):
        res = ''
        for i in range(26):
            self.let = chr(self.A+i)
            num = i+1
            res += f'{str(num)}, {self.let}, '
            # res += self.let
        return res

inf = Inf()
for _ in range(int(input('Введете число повторений: '))):
    print(next(inf), end=' ')