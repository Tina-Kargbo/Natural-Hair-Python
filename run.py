
#This code was inspired by the Code Institute's love_sandwiches challenge.

import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('natural_hair_products')

def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, seperated by commas.")
        print("Example: 23, 75, 20, 50, 87, 32\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")
    
        if validate_data(sales_data): 
            print("Data is valid")
            break

    return sales_data
    
def validate_data(values):
    """
    Inside the try, converts all string values into integers. 
    Raises ValueError if strings cannot be converted into int, or if they 
    aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) !=6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")   
        return False

    return True 

def update_sales_worksheet(data):

    print("updating sales worksheet...\n") 
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)

def calculate_suplus_data(sales_row):
    """
    Compare sales data and calculate for each data type
    """

    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(stock_row)

def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_suplus_data(sales_data)


print("Welcome to Natural Hair Products Data Automation")
main()