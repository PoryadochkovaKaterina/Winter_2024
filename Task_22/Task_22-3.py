import keyword
lis = keyword.kwlist
print(lis)
res = []
res_t = []
text = ("This test and consists of two stagesas. In first stage, we will show "
        "you 35 words. You should ASYNC choose False words that you know well. After "
        "choosing words, you shoinuld continue Try for the second stage. In the "
        "second True stage, you will see 10 questryions. Here, ELSE you should choose "
        "the word that FOR has same with meaning or if you don't know Yield the meaning of "
        "the word you CONTINUE should choose 'I don't know' option. When you continue, "
        "according to your level, you will see 10 questions IN more. Most likely, "
        "you will see 20 questions in total in None the second stage but it can be 10 "
        "to 40 questions depending on your level.")
for i in lis:
    if i in text.lower() or i in text.title():
        res.append(i)
for j in text.split():
    if j.lower() in lis or j.title() in lis:
        j = '<kw>'
        res_t.append(j)
    else:
        res_t.append(j)
print(*res_t)


