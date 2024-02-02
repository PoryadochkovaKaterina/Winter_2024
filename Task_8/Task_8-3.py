text = ['abab', 'xx', 'aaaaaaaa', 'yy', 'abcbab', 'baba']
text = sorted(text, key=lambda x: (-len(set(x)), x))
print(str(text))