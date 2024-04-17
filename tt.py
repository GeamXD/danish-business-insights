import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Function to download data in batches
def download_data_in_batches(url, headers, auth, query, batch_size=100):
    offset = 0
    all_hits = []
    
    # Define retry strategy
    retry_strategy = Retry(
        total=5,  # Total number of retries
        status_forcelist=[429, 500, 502, 503, 504],  # HTTP status codes to retry
        backoff_factor=1  # Exponential backoff factor
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)

    while True:
        # Add "size" and "from" parameters to control pagination
        body = query.copy()
        body["size"] = batch_size
        body["from"] = offset

        session = requests.Session()
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        response = session.post(url, json=body, headers=headers, auth=auth, timeout=30)

        if response.status_code == 200:
            data = response.json()
            hits = data['hits']['hits']
            if not hits:  # Break the loop if no more hits
                break
            all_hits.extend(hits)
            offset += batch_size
        else:
            print("Failed to retrieve data from the URL:", response.status_code)
            break

    return all_hits

# Function to parse hits into DataFrame
def parse_hits_to_dataframe(hits):
    parsed_data = []

    for hit in hits:
        cvr_nummer = hit['_source']['Vrvirksomhed']['cvrNummer']
        navn = hit['_source']['Vrvirksomhed']['navne'][0]['navn']
        kommune_navn = hit['_source']['Vrvirksomhed']['beliggenhedsadresse'][0]['kommune']['kommuneNavn']

        parsed_data.append({'CVR Nummer': cvr_nummer, 'Navn': navn, 'Kommune Navn': kommune_navn})

    return pd.DataFrame(parsed_data)

# Endpoint URL and authentication credentials
url = 'http://distribution.virk.dk/cvr-permanent/virksomhed/_search'
username = 'SafeOdds_CVR_I_SKYEN'
password = '7080bee8-7809-423e-9bd7-73d669f0cfde'

# Query for documents in Slagelse
query = {
  "query": {
    "match": {
      "Vrvirksomhed.beliggenhedsadresse.kommune.kommuneNavn": "SLAGELSE"
    }
  }
}

# Additional headers if required
headers = {
    'Content-Type': 'application/json',
}

# Download data in batches
hits = download_data_in_batches(url, headers, HTTPBasicAuth(username, password), query)

# Parse hits into DataFrame
df = parse_hits_to_dataframe(hits)

# Save DataFrame to CSV
df.to_csv('slagelse_dattta.csv', index=False)
