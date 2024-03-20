def compare(text1, text2, cou = 0):
    if text1 == text2:
        print('True')
    elif text1 in text2 and (len(text2) - len(text1) <= 1):
        print('True')
    elif text2 in text1 and (len(text1) - len(text2) <= 1):
        print('True')
    elif len(text1) == len(text2):
        for i in text1:
            for j in text2:
                if i == j:
                    cou += 1
                    if len(text1) - cou == 1:
                        print('True')
    else: print('False')

compare(input(), input())