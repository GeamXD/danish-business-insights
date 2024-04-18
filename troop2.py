import json
import pandas as pd

def extract_data_from_files(files):
    data_list = []
    for file in files:
        with open(file, 'r') as f:
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

def save_as_csv(data_list, output_filename='output_2.csv'):
    df = pd.DataFrame(data_list)
    df.to_csv(output_filename, index=False)
    print(f"Data saved as '{output_filename}'")

if __name__ == "__main__":
    filenames = ['custom_json/custom_1.json', 'custom_json/custom_2.json']  # Add more filenames as needed
    data_list = extract_data_from_files(filenames)
    save_as_csv(data_list)