# import itertools
# for x in itertools.permutations([1, 1, 3]):
#     print(x, end=' ')

# import itertools
# for x in itertools.combinations([1, 2, 3, 4], 4):
#     print(x, end=' ')

# import itertools
# for x in itertools.combinations_with_replacement([1, 2, 3, 4], 3):
#     print(x, end= ' ')

# import itertools
# x = itertools.cycle([1, 2, 3, 4])
# for _ in range(10):
#     print(next(x), end = ' ')

# import itertools
# for x in itertools.chain([1, 2, 3], 'abc', {10: 100, 20: 200, 30: 300}):
#     print(x, end=' ')

# import itertools
# for x in itertools.combinations_with_replacement('aabb', 4):
#     print(x, end=' ')

class SimpleIterator:
    def __init__(self):
        self.counter = 1
        self.next = 1
        self.res = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.counter = self.next
        self.next = self.res
        self.res = self.counter + self.next
        return self.res

s_iter2 = SimpleIterator()
for i in range(10):
    print(next(s_iter2))