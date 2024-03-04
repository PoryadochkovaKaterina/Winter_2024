# a = ('Python', 'Java')
# b = ('Python',)
# c = ('Python')
# print(type(a))
# print(type(b))
# print(type(c))

# class A:
#     def __init__(self, limit):
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.limit <= 0:
#             raise StopIteration
#         else:
#             self.limit -= 1
#             #print(self.limit)
#             return self.limit
# b = A(10)
# for _ in range(10):
#     print(next(b))
# for i in b:
#     print(i)



