import os
from datetime import date, datetime, timedelta

# create text file with date
def create_date_txt():
    if os.path.exists('date.txt') == False:
        current_date = date.today()
        current_date = current_date.strftime("%Y-%m-%d")
        file = open('date.txt', 'w')
        file.write(current_date)
        file.close()

# get current date
def get_date():
    with open('date.txt') as file:
        lines = file.readlines()
        current_date = lines[0]
        return current_date

# get advanced date 
def get_advance_date(number_of_dates): 
    today = get_date()
    today = datetime.strptime(today, '%Y-%m-%d')
    today.strftime('%Y-%m-%d')
    if number_of_dates < 0:
        number_of_dates = abs(number_of_dates)
    else:
        number_of_dates = f"-{number_of_dates}"
        number_of_dates = int(number_of_dates)
    advanced_date = today - timedelta(number_of_dates)
    advanced_date = advanced_date.strftime("%Y-%m-%d")
    file = open('date.txt', 'w')
    file.write(advanced_date)
    file.close()
    return advanced_date
