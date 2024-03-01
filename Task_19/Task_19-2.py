class Fibonacci:
    def __init__(self):
        self.current = 1
        self.next = 1
        self.res = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.current = self.next
        self.next = self.res
        self.res = self.current + self.next
        return self.res

fibonacci = Fibonacci()
for i in range(10):
    print(next(fibonacci))

# class Fibo:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a, self.b = self.b, self.b + self.a
#         return self.a
#
# fibo = Fibo()
# for _ in range(10):
#     print(next(fibo), end=' ')
