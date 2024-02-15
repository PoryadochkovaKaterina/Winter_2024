def leight(st, cou=0):
    print(st, cou)
    if len(st) <= 0:  # Граничный случай
        return
    else:  # Рекурсивный случай
        cou += 1
        leight(st[:-1], cou)
leight(input())
print()



cou = 0
def len_2(st):
    # print(st, cou)
    if len(st) <= 0:
        return
    else:
        global cou
        cou += 1
        len_2(st[:-1])

len_2(input())
print(cou)