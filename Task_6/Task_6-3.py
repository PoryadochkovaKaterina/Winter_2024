import string
n = input()
w, p, d = [], [], []
for i in n:
    if i in string.ascii_letters:
        w.append(i)
    if i in string.punctuation:
        p.append(i)
    if i in string.digits:
        d.append(i)
print(' '.join(set(w)))
print(' '.join(set(d)))
print(' '.join(set(p)))