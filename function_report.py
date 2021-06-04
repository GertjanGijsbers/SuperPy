import os
import csv
from prettytable import PrettyTable
from my_date import get_date, get_advance_date
from rich import print

# read a .csv file 
def read_file(file_name):
    # get location file
    folder = os.getcwd()
    file = os.path.join(folder, 'csv-files', f'{file_name}.csv')
    # read the file
    f = open(file, "r")
    for x in f:
        if x is not None:
            return f.read()
        else:
            return f"[bold red]:warning: No rows in file: {file_name}.csv[/bold red]"

# convert a CSV file to a list 
def convert_csv_to_list(file_name):
    folder = os.getcwd()
    file = os.path.join(folder, 'csv-files', f'{file_name}.csv')
    with open(file, newline='') as f:
        next(f)
        reader = csv.reader(f)
        data = list(reader)
    return data

# create a PrettyTable response of the inventory
def report_inventory():
    f = convert_csv_to_list('bought')
    t = PrettyTable(['Product Name', 'Count', 'Buy Price', 'Expiration Date'])
    for x in f:
        product_name = x[1]
        buy_price = x[3]
        expiration_date = x[4]
        t.add_row([product_name, 1, buy_price, expiration_date])
    t.sortby = "Product Name"
    return(t)

# create a PrettyTable response of the revenue
def report_revenue(given_date):
    f = convert_csv_to_list('bought')
    t = PrettyTable(['Product Name', 'Buy Date', 'Buy Price', 'Expiration Date'])
    if given_date == 'today':
        for x in f:
            today_check = get_date()
            today_loop = x[2]
            if today_loop == today_check:
                product_name = x[1]
                buy_date = x[2]
                buy_price = x[3]
                expiration_date = x[4]
                t.add_row([product_name, buy_date, buy_price, expiration_date])
    elif given_date == 'yesterday':
        for x in f:
            yesterday_check = get_advance_date(1)
            yesterday_loop = x[2]
            if yesterday_loop == yesterday_check:
                product_name = x[1]
                buy_date = x[2]
                buy_price = x[3]
                expiration_date = x[4]
                t.add_row([product_name, buy_date, buy_price, expiration_date])
    else:
        for x in f:
            if type(given_date) == str:
                specific_date_check = given_date
            else:
                raise TypeError("[bold red]:warning: Buy date needs to be a string[/bold red]")
            specific_date_loop = x[2]
            if specific_date_loop == specific_date_check:
                product_name = x[1]
                buy_date = x[2]
                buy_price = x[3]
                expiration_date = x[4]
                t.add_row([product_name, buy_date, buy_price, expiration_date])
    t.sortby = "Product Name"
    return(t)

# create a PrettyTable response of the profit
def report_profit(given_date):
    file_bought = convert_csv_to_list('bought')
    file_sold = convert_csv_to_list('sold')
    # check the sum of the sales
    amount_sales = 0.0
    amount_costs = 0.0
    for x in file_sold:
        if given_date == 'today':
            today = get_date()
            if x[2] == today:
                amount_sales += float(x[3])
                for y in file_bought:
                    if x[1] == y[0]:
                        amount_costs += float(y[3])
        elif given_date == 'yesterday':
            yesterday = get_advance_date(1)
            if x[2] == yesterday:
                amount_sales += float(x[3])
                for y in file_bought:
                    if x[1] == y[0]:
                        amount_costs += float(y[3])
        else:
            specific_date = given_date
            if x[2] == specific_date:
                amount_sales += float(x[3])
                for y in file_bought:
                    if x[1] == y[0]:
                        amount_costs += float(y[3])
    # sales minus the costs
    total_profit = amount_sales - amount_costs
    total_profit = ("{:.2f}".format(round(total_profit, 2)))

    return f"[bold blue]:euro: €{total_profit}[bold blue]"
