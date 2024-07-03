import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.playbook

# Function to read each sheet from Excel and import into MongoDB
def import_excel_to_mongodb(excel_file):
    # Read Excel file
    xls = pd.ExcelFile(excel_file)
    # Iterate over each sheet
    for sheet_name in xls.sheet_names:
        # Read sheet
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        # Convert to JSON
        json_str = df.to_json(orient='records', force_ascii=False)
        # Convert JSON string to Python dictionary
        json_data = pd.read_json(json_str)
        # Convert dataframe to dictionary
        data_dict = json_data.to_dict(orient='records')
        # Insert data into MongoDB
        db[sheet_name].insert_many(data_dict)
        print(f"Data from '{sheet_name}' sheet imported into MongoDB successfully.")


# Specify the Excel file
excel_file = 'playbook_excel.xlsx'

# Call the function to import data into MongoDB
import_excel_to_mongodb(excel_file)


# import pandas
#
# excel_data_df = pandas.read_excel('playbook_excel.xlsx', sheet_name='оcтановился коннектор')
# json_str = excel_data_df.to_json(orient='records', force_ascii=False)
# print(json_str)