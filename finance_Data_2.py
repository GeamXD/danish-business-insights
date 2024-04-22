import requests
import pandas as pd
from bs4 import BeautifulSoup
import json


def extract_financial_data_from_links(file_path):
    # Create an empty dictionary to store data
    data = {
        'Name and Surname of Chairman': [],
        'Date of Approval of Annual Report': [],
        'Place of Signature of Statement': [],
        'Information on Type of Submitted Report': [],
        'Identification Number CVR of Reporting Entity': [],
        'Name of Reporting Entity': [],
        'Address of Reporting Entity': [],
        'Name of Financial Institution': [],
        'Name of Audit Firm': [],
        'Address of Auditor': [],
        'Identification of Approved Annual Report': [],
        'Confirmation That Annual Report Is Presented': [],
        'Confirmation That Financial Statements Are Exempted': [],
        'Confirmation That Financial Statement Gives True and Fair View': [],
        'Recommendation for Approval of Annual Report': [],
        'Information on Reporting Class of Entity': [],
        'Description of General Matters Related to Recognition Measurement': [],
        'Description of Methods of Recognition and Measurement Basis of Income Statement Items': [],
        'Description of Methods of Recognition and Measurement Basis of External Expenses': [],
        'Description of Methods of Recognition and Measurement Basis of Finance Income and Expenses': [],
        'Description of Methods of Recognition and Measurement Basis of Tax Expenses': [],
        'Description of Methods of Recognition and Measurement Basis of Assets and Liabilities': [],
        'Description of Methods of Recognition and Measurement Basis of Receivables': [],
        'Description of Methods of Dividends': [],
        'Description of Methods of Recognition and Measurement Basis of Tax Payables and Deferred Tax': [],
        'Description of Methods of Recognition and Measurement Basis of Liabilities Other Than Provisions': [],
        'Disclosure of Main Activities and Accounting and Financial Matters': [],
        'Disclosure of Equity': [],
        'Disclosure of Contingent Liabilities': [],
        'Disclosure of Mortgages and Collaterals': [],
        'Gross Profit Loss': [],
        'Profit Loss from Ordinary Operating Activities': [],
        'Other Finance Income': [],
        'Rest of Other Finance Expenses': [],
        'Profit Loss': [],
        'Short-term Tax Receivables': [],
        'Short-term Receivables': [],
        'Other Short-term Investments': [],
        'Short-term Investments': [],
        'Cash and Cash Equivalents': [],
        'Current Assets': [],
        'Assets': [],
        'Contributed Capital': [],
        'Retained Earnings': [],
        'Equity': [],
        'Short-term Debt to Banks': [],
        'Short-term Payables to Associates': [],
        'Short-term Liabilities Other Than Provisions': [],
        'Liabilities Other Than Provisions': [],
        'Liabilities and Equity': []
    }

    # Read links from the text file
    with open(file_path, 'r') as file:
        links = file.readlines()

    # Iterate through each link
    for link in links:
        link = link.strip()  # Remove leading/trailing whitespace
        response = requests.get(link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            context = soup.find_all()
            # print(context)
            # exit
            for tag in context:
                tag_name = tag.name.replace("{http://www.xbrl.org/2003/instance}", "")
                if tag_name in data:
                    data[tag_name].append(tag.text)
                else:
                    data[tag_name] = [tag.text] * len(data['Name and Surname of Chairman'])  # Assume the same length

    # Create a DataFrame
    # df = pd.DataFrame(data)
    # df.to_csv('csv_financial.csv')
    return data

# Example usage
file_path = 'sample.txt'  # Path to the text file containing XML links
financial_data_df = extract_financial_data_from_links(file_path)


with open('ai.json', 'w') as file:
    json.dump(financial_data_df, file)
# print(financial_data_df)
