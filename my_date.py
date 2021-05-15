from datetime import date, datetime, timedelta

# get current date
def get_date():
    current_date = date.today()
    current_date = current_date.strftime("%Y-%m-%d")
    return current_date

# get advanced date 
def get_advance_date(date): 
    today = get_date()
    today = datetime.strptime(today, '%Y-%m-%d')
    today.strftime('%Y-%m-%d')
    advanced_date = today - timedelta(date)
    advanced_date = advanced_date.strftime("%Y-%m-%d")
    return advanced_date