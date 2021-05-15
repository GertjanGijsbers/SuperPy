import argparse

def create_parser():
    # start with the first level of the parser
    parser = argparse.ArgumentParser(description="Keep track of your inventory.", formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(dest="command")

    # create an option to advance the date:
    parser.add_argument("--advance-date", type=int, help="advance the current date with the number of days you want to extract")

    # create the buy parser:
    buy_parser = subparsers.add_parser("buy", help="add product to inventory")
    buy_parser.add_argument("--product-name", type=str, help="insert product name")
    buy_parser.add_argument("--buy-date", help="insert when the product was purchased: YYYY-MM-DD")
    buy_parser.add_argument("--buy-price", type=float, help="insert buy price")
    buy_parser.add_argument("--expiration-date", help="insert when the product will expire: YYYY-MM-DD")

    # create the sell parser:
    sell_parser = subparsers.add_parser("sell", help="register sold product")
    sell_parser.add_argument("--product-name", type=str, help="insert product name")
    sell_parser.add_argument("--sell-date", help="insert when the product was sold: YYYY-MM-DD")
    sell_parser.add_argument("--sell-price", type=float, help="insert sell price")

    # create the report parser:
    report = subparsers.add_parser("report", help="report transactions")
    report_subparsers = report.add_subparsers(dest="report_subparsers")
    inventory = report_subparsers.add_parser("inventory", help="report inventory")
    revenue = report_subparsers.add_parser("revenue", help="report revenue")
    profit = report_subparsers.add_parser("profit", help="report profit")
    inventory.add_argument("--today", help="show current inventory")
    revenue.add_argument("--yesterday", action="store_true", help="reports the revenue of yesterday")
    revenue.add_argument("--today", action="store_true", help="reports the revenue made today")
    revenue.add_argument("--date", type=str, help="reports the revenue for a specific date: YYYY-MM-DD")
    profit.add_argument("--today", action="store_true", help="reports the profit of today")
    profit.add_argument("--yesterday", action="store_true", help="reports the profit of yesterday")
    profit.add_argument("--date", type=str, help="reports the profit of yesterday")

    # create the export parser:
    export = subparsers.add_parser("export", help="export your inventory")
    export_subparsers = export.add_subparsers(dest="export_subparsers")
    export = export_subparsers.add_parser("inventory", help="exports the inventory to a CSV and JSON file")

    return parser