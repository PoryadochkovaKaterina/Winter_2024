import psycopg2
import pandas as pd
con = psycopg2.connect(
    database='postgres',
    user='postgres',
    password=
    host='127.0.0.1',
    port='5432')

cur = con.cursor()
cur.execute('''SELECT * FROM book ORDER BY book_id ASC''')
rows = cur.fetchall()
names = list(map(lambda x: x[0], cur.description))
n = len(names)
columns_name = []
columns = []

for i in range(n):
    columns_name.append(names[i])
for i in range(n):
    columns.append([row[i] for row in rows])

dic = dict(zip(columns_name, columns))
len_col = len(columns[0])
# print(len_col)
# print(dic)

df = pd.DataFrame(dic, index=range(len_col))
print(df)

con.close()


