# public module
import os
import pandas
import csv
import json
from datetime import datetime
from rich import print
# local module
from function_report import convert_csv_to_list

# export the complete inventory to a CSV file
def export_inventory_csv():
    # get data in bought.csv
    f = convert_csv_to_list('bought')
    csv_file = pandas.DataFrame(f, columns=['ID', 'Product Name', 'Buy Date', 'Buy Price', 'Expiration Date'])
    # get datetime for file name
    date_file = datetime.now()
    date_file = date_file.strftime('%Y-%m-%d-(%H%M%S)')
    # get folder to export
    folder = os.getcwd()
    file = folder + f"\\exports\\inventory-{date_file}.csv"
    # export file
    csv_file.to_csv(file)
    # message export succeeded
    print(f'[bold magenta]Yes, file \'inventory-{date_file}.csv\' has been exported to folder \'exports\'[/bold magenta]')

# export the complete inventory to a json file
def export_inventory_json(csv_file_path, json_file_path, date_file):
    json_array = []
    #read csv file
    with open(csv_file_path, encoding='utf-8') as csv_file: 
        #load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csv_file) 
        #convert each csv row into python dict
        for row in csv_reader: 
            #add this python dict to json array
            json_array.append(row)
    #convert python jsonArray to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as json_file: 
        json_string = json.dumps(json_array, indent=4)
        json_file.write(json_string)
    csv_file_path = r'data.csv'
    json_file_path = r'data.json'
    # message export succeeded
    print(f'[bold blue]Yes, file \'inventory-{date_file}.json\' has been exported to folder \'exports\'[/bold blue]')