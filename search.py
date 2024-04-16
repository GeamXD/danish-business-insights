
import pprint
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
import json

url = 'http://distribution.virk.dk/cvr-permanent/virksomhed/_search'
url_2 = ''
headers = {
    'Content-Type': 'application/json',
    # Add any other headers if required
}
body = {
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "Vrvirksomhed.cvrNummer": "10150817"
                    }
                }
            ]
        }
    }
}

body_2 = {
  "query": {
    "match": {
      "Vrvirksomhed.beliggenhedsadresse.kommune.kommuneNavn": "SLAGELSE"
    }
  }
}

username = 'SafeOdds_CVR_I_SKYEN'
password = '7080bee8-7809-423e-9bd7-73d669f0cfde'

response = requests.post(url, json=body_2, headers=headers, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    data = response.json()
else:
    print("Failed to retrieve data from the URL:", response.status_code)

# Extract relevant information from the JSON response
hits = data['hits']['hits']
parsed_data = []

for hit in hits:
    cvr_nummer = hit['_source']['Vrvirksomhed']['cvrNummer']
    navn = hit['_source']['Vrvirksomhed']['navne'][0]['navn']
    kommune_navn = hit['_source']['Vrvirksomhed']['beliggenhedsadresse'][0]['kommune']['kommuneNavn']
    
    parsed_data.append({'CVR Nummer': cvr_nummer, 'Navn': navn, 'Kommune Navn': kommune_navn})

# Create DataFrame
df = pd.DataFrame(parsed_data)

# Convert DataFrame to CSV
df.to_csv('parsed_data.csv', index=False)

# Optionally, you can display the DataFrame
# print(df)
