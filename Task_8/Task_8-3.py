text = ['abab', 'xx', 'aaaaaaaa', 'abcbab']
text = sorted(text, key=lambda x: len(list(set(x))))
text.reverse()
print(str(text))