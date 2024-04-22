import os
import json
import pandas as pd

def extract_data_from_files(directory):
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):  # Filter only txt files, adjust if needed
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as f:
                for line in f:
                    data = json.loads(line)
                    cvr_nummer = data.get('_source', {}).get('Vrvirksomhed', {}).get('cvrNummer')
                    navn = data.get('_source', {}).get('Vrvirksomhed', {}).get('navne', [{}])[0].get('navn', '')
                    kommune_navn = data.get('_source', {}).get('Vrvirksomhed', {}).get('beliggenhedsadresse', [{}])[0].get('kommune', {}).get('kommuneNavn', '')
                    aarsbeskaeftigelse = data.get('_source', {}).get('Vrvirksomhed', {}).get('aarsbeskaeftigelse', [])
                    if aarsbeskaeftigelse:
                        antal_ansatte = aarsbeskaeftigelse[0].get('antalAnsatte', '')
                    else:
                        antal_ansatte = ''
                    data_list.append({
                        'cvr_nummer': cvr_nummer,
                        'navn': navn,
                        'kommune_navn': kommune_navn,
                        'antal_ansatte': antal_ansatte
                    })
    return data_list

def save_as_csv(data_list, output_filename='final_output.csv'):
    df = pd.DataFrame(data_list)
    df.to_csv(output_filename, index=False)
    print(f"Data saved as '{output_filename}'")

if __name__ == "__main__":
    directory = '/workspace/danish-business-insights/jsons'  # Change to your directory path
    data_list = extract_data_from_files(directory)
    save_as_csv(data_list)
