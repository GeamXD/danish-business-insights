import json
import pandas as pd

def extract_data_from_line(line):
    # Parse the JSON on each line into a dictionary
    data = json.loads(line)
    
    # Extract the desired data from the dictionary
    cvr_nummer = data.get('_source', {}).get('Vrvirksomhed', {}).get('cvrNummer')
    navn = data.get('_source', {}).get('Vrvirksomhed', {}).get('navne', [{}])[0].get('navn', '')
    kommune_navn = data.get('_source', {}).get('Vrvirksomhed', {}).get('beliggenhedsadresse', [{}])[0].get('kommune', {}).get('kommuneNavn', '')
    
    # Check if aarsbeskaeftigelse list is empty
    aarsbeskaeftigelse = data.get('_source', {}).get('Vrvirksomhed', {}).get('aarsbeskaeftigelse', [])
    if aarsbeskaeftigelse:
        antal_ansatte = aarsbeskaeftigelse[0].get('antalAnsatte', '')
    else:
        antal_ansatte = ''

    return {
        'cvr_nummer': cvr_nummer,
        'navn': navn,
        'kommune_navn': kommune_navn,
        'antal_ansatte': antal_ansatte
    }


def save_as_pandas(data_list):
    df = pd.DataFrame(data_list)
    df.to_csv('output.csv', index=False)
    print("Data saved as 'output.csv'")

# Open the file in read mode
with open('custom_1.json', 'r') as file:
    data_list = []
    # Iterate over each line in the file
    for line in file:
        # Extract data from the line
        extracted_data = extract_data_from_line(line)
        data_list.append(extracted_data)

# Save extracted data as pandas DataFrame
save_as_pandas(data_list)
