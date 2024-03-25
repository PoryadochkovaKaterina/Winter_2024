def inversion(spisok, cou=0):
    for i, v in enumerate(spisok):
        for j, k in enumerate(spisok):
            if i < j and spisok[i] > spisok[j]:
                # print(i, v, j, k)
                print(v, k)
                cou += 1
    return cou

# print(inversion([5, 4, 3, 2, 1]))
# print(inversion([1, 2, 3, 4, 5]))
# print(inversion([1, 4, 3, 0, 5]))
# print(inversion([10, 5, 3, 6, 7]))
print(inversion([0, 3, 4, 2, 0, 2]))