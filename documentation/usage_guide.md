## Usage guide 
A text file containing a usage guide aimed with peers as the target audience. The usage guide should include plenty of examples. <br><br>

# <b>Example 1</b>
Start by exploring the SuperPy by searching what kind of arguments the program offers. 

<u>Command line:</u>

```
python main.py --help
```
<u>Response:</u>

```
usage: main.py [-h] [--advance-date ADVANCE_DATE]
               {buy,sell,report,export} ...

Keep track of your inventory.

positional arguments:
  {buy,sell,report,export}
    buy                 add product to inventory
    sell                register sold product
    report              report transactions
    export              export your inventory

optional arguments:
  -h, --help            show this help message and exit
  --advance-date ADVANCE_DATE
                        advance the current date with the number of days you want to extract
```
<br><br>

# <b>Example 2</b>
You're able to add products to the inventory by using 'buy'.

<u>Command line:</u>

```
python main.py buy --product-name cheese --buy-date 2002-10-01 --buy-price 0.8 --expiration-date 2020-01-01
```
<u>Response:</u>

```
👍 Product cheese added to bought.csv
```

<br><br>

# <b>Example 3</b>
You're able to sell products from your inventory by using 'sell'.

<u>Command line:</u>

```
python main.py sell --product-name cheese --sell-price 1.8
```
<u>Response:</u>

```
👍 Product cheese added to sold.csv
```

<br><br>

# <b>Example 4</b>
You're able to report products from your inventory by using 'report'. In this example do we report the profit of a specific date. You're also able to report the inventory and revenue.

<u>Command line:</u>

```
python main.py report profit --date 2020-02-02
```
<u>Response:</u>

```
💶 €2.00
```

<br><br>

# <b>Example 5</b>
You're able to export your inventory by using 'export'. The files will be downloaded in your local file. The program exports a CSV file and a JSON file.

<u>Command line:</u>

```
python main.py export inventory
```
<u>Response:</u>

```
Yes, file 'inventory-2021-05-15-(171207).csv' has been exported to folder 
'exports'
Yes, file 'inventory-2021-05-15-(171207).json' has been exported to folder 
'exports'
```

<br><br>