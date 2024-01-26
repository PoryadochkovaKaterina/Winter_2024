# for i in 'Hello world!':
#    print(i, end = '*')

# for j in range(5):
#    print(j)
# for k in range (-5, 5):
#    print(k, end = ',')
# for n in range (5, -5, -2):
#    print(n)

# for i in range(10):
#    if i % 2 == 0 :
#        print(i,'- Четное')
#    else:
#        print(i, '- Нечетное')

# n = int(input())
# for n in range(1, n + 1):
#     if n % 15 == 0:
#         print('FizzBuzz', end=' ')
#     elif n % 3 == 0:
#         print('Fizz', end=' ')
#     elif n % 5 == 0:
#         print('Buzz', end=' ')
#     else: print(n, end=' ')

# for k in 'Hello world':
#     if k == 'a':
#         break
# else:
#     print('Нет такой буквы')

# n = int(input())
# for i in range(1, n+1):
#     for j in range(i):
#         print('+', end='')
#     print()

# s = ['Hello']
# s1 = list('Hello')
# print(s, '\n', s1)

# m = [4, 5, 7, 9]
# m[0] = 3
# print(len(m), m)

# for j in m: # Элементы списка
#    print(j)

# for j in range(len(m)): # Элементы списка, использование индексов значений в списке
#    print(m[j])

# i_lis = [10, [15, 2], 'ABC', 1]
# for x in i_lis:
#     if type(x) == str:
#         print(x * 2)
#     elif type(x) == int:
#         print(x ** 2)
#     else: print(x)

# a = []
# a.append('Hello')
# a.append(3)
# print(a)

ls = []
for i in range(5):
    a = int(input())
    ls.append(a)
    print(ls)
