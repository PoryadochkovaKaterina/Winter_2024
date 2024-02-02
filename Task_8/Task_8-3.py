def len_fun(val):
    return len(list(set(val)))

text = ['abab', 'xx', 'aaaaaaaa', 'abcbab']
text = sorted(text, key=len_fun)
text.reverse()
print(str(text))