import pandas as pd
import re
def sum_Data(lst):
    df = pd.DataFrame(lst)
    res = []
    for i in df.index:
        for j in df.columns:
            # res_n = isinstance(df.loc[i, j], int)
            if re.findall(r'(\b\d+\b)|(\b\d+.\d+\b)|(\b\d+,\d+\b)', df.loc[i, j]):
                # print(type(df.loc[i, j]))
                res.append(float(df.loc[i, j]))
    return sum(res)
print(sum_Data(input().split()))


# s = 0
# for i in df.index:
#     for j in df.columns:
#         #if type(df.loc[i, j]) == np.int64 or type(df.loc[i, j]) == np.floot64:
#         try:
#             s += df.loc[i, j]
#         except:
#             pass
# print(s)
