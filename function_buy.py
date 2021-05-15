import csv
import os
from rich import print

def buy(product_name, buy_date, buy_price, expiration_date):
    # get location file
    folder = os.getcwd()
    file = folder + f"\\csv-files\\bought.csv"
    # read file and get number of lines for the id
    f = open(file)
    reader = csv.reader(f)
    lines = len(list(reader))
    # append a new row to the bought file
    row = [lines, product_name, buy_date, buy_price, expiration_date]
    with open(file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        print(f"[bold green]:thumbsup: Product {product_name} added to bought.csv")
