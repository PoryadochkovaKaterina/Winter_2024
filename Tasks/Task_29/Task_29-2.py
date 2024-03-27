str_1 = 'abc'
# str_2 = 'abc'
# str_2 = 'abd'
# str_2 = 'adb'
# str_2 = 'dbc'
str_2 = 'xyz'

print(sum(1 if i == j and v != k else 0 for i, v in enumerate(str_1) for j, k in enumerate(str_2)))

print(sum([i != j for i, j in zip(str_1, str_2)]))