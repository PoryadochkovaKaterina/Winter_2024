dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

def rim(num):
    res = ''
    for i, v in dict.items():
        while num >= v:
            res += i
            num -= v
    return res


print(rim(int(input())))