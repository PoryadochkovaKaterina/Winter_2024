import calendar
from datetime import date, time
year = int(input())
res = []
for mon in range(1, 13):
    c = 0
    p = calendar.monthcalendar(year, mon)  # календарь на месяц в виде мнгогострочной матрицы
    for week in p:
        thu = week[3]
        if thu:
            c += 1
            if c == 3:
                dat = date(year, mon, thu)
                res.append(dat.strftime('%d.%m.%y'))
                c = 0
print(*res, sep='\n')
