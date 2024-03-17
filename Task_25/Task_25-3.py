# import camelcaser as cc
# input_word = "verry long test exampLe"
#
# camel_case = cc.make_camel_case(input_word)
# print(f"Camel case: {camel_case}")

text = "vERry loNg Test eXAmpLe".lower().split(' ')
res = ''
for i in text:
    res += i.title()
print(res)