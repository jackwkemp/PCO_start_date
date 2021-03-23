import datetime

expiry_date = '22/04/2022'

exp_day = datetime.datetime.strptime(expiry_date, '%d/%m/%Y').strftime('%d')

month = datetime.datetime.strptime(expiry_date, '%d/%m/%Y').strftime('%m')

year = datetime.datetime.strptime(expiry_date, '%d/%m/%Y').strftime('%Y')

start_day = str(int(exp_day) + 1)

start_month = month

start_year = str(int(year) - 3)

start_date = start_day + "/" + start_month + "/" + start_year

print(start_date)
