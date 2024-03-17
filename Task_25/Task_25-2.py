def is_pal(string):
    if len(string) <= 1:
        return 'True'
    if string[0] != string[-1]:
        return 'False'
    return is_pal(string[1:-1])

print(is_pal(''.join(input().lower().split())))

