# for i in range(1, 10+1):
#     for j in range(i):
#         print(i, end=' ')

lst = [i for i in range(1, 10+1) for j in range(i)]
print(*lst)


