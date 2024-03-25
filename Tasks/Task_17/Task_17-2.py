def fu(func):
    def wra(*args, **kwargs):
        # print(args)   # позиционный аргумент
        # print(kwargs)   # именованный аргумент
        val = func(*args, **kwargs)
        res = []
        for x in args:
            if type(x) == str:
                x = x.upper()
                res.append(x)
        for k, v in kwargs.items():
            if type(k) == str and type(v) == str:
                k = k.upper()
                v = v.upper()
                res.append((k, v))
            elif type(v) == str:
                v = v.upper()
                res.append((k, v))
            elif type(k) == str:
                k = k.upper()
                res.append((k, v))
        # print(res)
        return res
    return wra

@fu
def text(*args, **kwargs):
    return
print(text('1', 2, '7', 6, '3', x = '4', y = 5, b = 'def'))




