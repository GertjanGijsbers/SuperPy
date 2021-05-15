from rich import print

# let's check if the parameters contain the right data type for buy
def check_parameters_buy(product_name, buy_date, buy_price, expiration_date):
    if not isinstance(product_name, str):
        raise TypeError('[bold red]:warning: The data type for parameter product_name is incorrect. This should be a string[/bold red]')
    if not isinstance(buy_date, str):
        raise TypeError('[bold red]:warning: The data type for parameter buy_date is incorrect. This should be a string: YYYY-MM-DD[/bold red]')
    if not isinstance(buy_price, float):
        raise TypeError('[bold red]:warning: The data type for parameter buy_price is incorrect. This should be a float[/bold red]')
    if not isinstance(expiration_date, str):
        raise TypeError('[bold red]:warning: The data type for parameter expiration_date is incorrect. This should be a string: YYYY-MM-DD[/bold red]')

# let's check if the parameters contain the right data type for sell
def check_parameters_sell(product_name, sell_date, sell_price):
    if not isinstance(product_name, str):
        raise TypeError('[bold red]:warning: The data type for parameter product_name is incorrect. This should be a string[/bold red]')
    if not isinstance(sell_date, str):
        raise TypeError('[bold red]:warning: The data type for parameter sell_date is incorrect. This should be a string: YYYY-MM-DD[/bold red]')
    if not isinstance(sell_price, float):
        raise TypeError('[bold red]:warning: The data type for parameter sell_price is incorrect. This should be a float[/bold red]')
