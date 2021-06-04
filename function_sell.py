import csv
import os
import datetime
from rich import print

def sell(product_name, sell_date, sell_price):
    # get location file
    folder = os.getcwd()
    file_bought = os.path.join(folder, 'csv-files', 'bought.csv')
    file_sold = os.path.join(folder, 'csv-files', 'sold.csv')
    # read file and get the bought_id matching the product_name
    check_loop = "No match found"
    with open(file_bought) as f:
        for i, line in enumerate(f):
            if product_name in line:
                bought_id = i
                check_loop = "Match found" # change variable 
                break
    # finaly, if the variable is still the same. Than the loop didn't match an excisting product 
    if check_loop == "No match found":
        raise TypeError(f"[bold red]:warning: No can't do. There is no product with the name {product_name} in bought.csv[/bold red]")
    # get the id (index) number for the next line
    f = open(file_sold)
    reader = csv.reader(f)
    lines = len(list(reader))
    # write sold product to the sold.csv file
    row = [lines, bought_id, sell_date, sell_price]
    with open(file_sold, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        print( f"[bold green]:thumbsup: Product {product_name} added to sold.csv[/bold green]")
