bracket = input()
op = 0
cl = 0
for i in bracket:
    # print(i)
    if len(bracket) % 2 != 0 or bracket[0] == ')':
        print('False')
        break
    if i == '(':
        op += 1
        cl = op
        # print(op, cl)
    elif i == ')':
        cl -= 1
        op -= 1
        if (cl and op) < 0:
            print('False')
            break
        # print(op, cl)
if op == cl == 0 and bracket[0] != ')' and len(bracket) % 2 == 0:
    print('True')
