def lower(func):
    def wrp():
        orig_res = func()
        mod_res = orig_res.lower()
        return mod_res
    return wrp
@lower
def text():
    return input()
print(text())