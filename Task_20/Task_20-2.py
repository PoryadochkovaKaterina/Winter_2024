import pandas as pd
def sum_Data(lst):
    df = pd.DataFrame(lst)
    res = []
    for i in df.index:
        for j in df.columns:
            # print(type(df.loc[i, j]), df.loc[i, j])
            if not df.loc[i, j].isalpha():
                res.append(float(df.loc[i, j]))
    return sum(res)
print(sum_Data(input().split()))

