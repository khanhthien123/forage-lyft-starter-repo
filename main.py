from datetime import date

today = date(2020, 8, 10)
yesterday = date(2018, 11, 3)
print(today.toordinal() - yesterday.toordinal())