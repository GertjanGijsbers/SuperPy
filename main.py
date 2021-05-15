# local modules
from my_parser import create_parser
from my_date import get_date, get_advance_date
from test_main import check_parameters_buy, check_parameters_sell
from function_buy import buy
from function_sell import sell
from function_report import report_inventory, report_revenue, report_profit
from function_export import export_inventory_csv, export_inventory_json
# public module
from rich import print
from datetime import datetime
import os

# do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'

if __name__ == '__main__':
    # use the parser function for the command line
    parser = create_parser()
    args = parser.parse_args()

    # optional argument --advance-time
    if args.advance_date:
        adjust_date = args.advance_date
        today = get_advance_date(adjust_date)
        print(f"[bold magenta]You've changed the date to {today}.[/bold magenta] :smile:")

    
    # positional argument buy
    if args.command == 'buy':
        product_name = args.product_name
        if args.buy_date != "":
            buy_date = get_date()
        else:
            buy_date = args.buy_date
        buy_price = args.buy_price 
        expiration_date = args.expiration_date
        # check if the parameters are valid
        check_parameters_buy(product_name, buy_date, buy_price, expiration_date)
        # add product to inventory
        buy(product_name, buy_date, buy_price, expiration_date)
    
    # positional argument sell
    if args.command == 'sell':
        product_name = args.product_name
        if args.sell_date != "":
            sell_date = get_date()
        else:
            sell_date = args.sell_date
        sell_price = args.sell_price 
        # check if the parameters are valid
        check_parameters_sell(product_name, sell_date, sell_price)
        # add product to inventory
        sell(product_name, sell_date, sell_price)
    
    # positional argument report
    if args.command == 'report':
        # optional argument --inventory
        if args.report_subparsers == 'inventory':
            print(report_inventory())
        # optional argument --revenue
        if args.report_subparsers == 'revenue':
            if args.today == True:
                given_date = 'today'
            elif args.yesterday == True:
                given_date = 'yesterday'
            else:
                given_date = args.date
            print(report_revenue(given_date))
        # optional argument --profit
        if args.report_subparsers == 'profit':
            if args.today == True:
                given_date = 'today'
            elif args.yesterday == True:
                given_date = 'yesterday'
            else:
                given_date = args.date
            print(report_profit(given_date))
    
    # positional argument export
    if args.command == 'export':
        if args.export_subparsers == "inventory":
            # export csv
            export_inventory_csv()
            # export json
            folder = os.getcwd()
            csv_file_path = folder + f"\\csv-files\\bought.csv"
            date_file = datetime.now()
            date_file = date_file.strftime('%Y-%m-%d-(%H%M%S)')
            json_file_path = folder + f"\\exports\\inventory-{date_file}.json"
            export_inventory_json(csv_file_path, json_file_path, date_file)