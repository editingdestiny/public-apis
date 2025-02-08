import requests
import json
import pandas as pd
from tabulate import tabulate

def get_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None

# API key
api_key = "OBTUAcgLJAq5OI9sq1QGj1MKG3RsGswl"

# 1. Get the list of companies
companies_url = f"https://financialmodelingprep.com/api/v3/stock/list?apikey={api_key}"
companies_data = get_api_data(companies_url)

if not companies_data:
    print("Failed to retrieve company list.")
    exit()

# 2. Create a "dropdown" (printed list)
print("Available Companies:")
for i, company in enumerate(companies_data[:10]):  # Limit to first 10 for brevity
    print(f"{i+1}. {company['symbol']} - {company['name']}")

# 3. User selects a company
while True:
    try:
        choice = int(input("Enter the number of the company to get financial statements (or 0 to exit): "))
        if choice == 0:
            exit()
        if 1 <= choice <= len(companies_data[:10]):
            selected_company = companies_data[choice-1]['symbol']
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# 4. Retrieve financial statements
income_statement_url = f"https://financialmodelingprep.com/api/v3/income-statement/{selected_company}?period=annual&apikey={api_key}"
balance_sheet_url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{selected_company}?period=annual&apikey={api_key}"

income_statement_data = get_api_data(income_statement_url)
balance_sheet_data = get_api_data(balance_sheet_url)

if income_statement_data:
    print("\nIncome Statement:")
    # Convert to DataFrame and display as table
    income_df = pd.DataFrame(income_statement_data)
    print(tabulate(income_df, headers='keys', tablefmt='psql'))
    print("\nDataFrame View:")
    print(income_df.head())  # Display the first few rows of the DataFrame
else:
    print("Failed to retrieve income statement.")

if balance_sheet_data:
    print("\nBalance Sheet:")
    # Convert to DataFrame and display as table
    balance_df = pd.DataFrame(balance_sheet_data)
    print(tabulate(balance_df, headers='keys', tablefmt='psql'))
    print("\nDataFrame View:")
    print(balance_df.head())  # Display the first few rows of the DataFrame
else:
    print("Failed to retrieve balance sheet.")
