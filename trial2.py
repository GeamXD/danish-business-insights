import json
import requests
from requests.auth import HTTPBasicAuth

def retrieve_data_and_append_to_json(url, auth, query, filename, batch_size=100):
    scroll_timeout = "1m"
    scroll_url = f"{url}/_search?scroll={scroll_timeout}"

    headers = {
        'Content-Type': 'application/json',
    }

    # Initial search request
    response = requests.post(scroll_url, json=query, headers=headers, auth=auth)
    if response.status_code != 200:
        print("Failed to retrieve data from the URL:", response.status_code)
        return

    scroll_id = response.json().get("_scroll_id")
    hits = response.json()['hits']['hits']
    append_to_json(hits, filename)

    # Continue retrieving batches using scroll API
    while True:
        scroll_request = {
            "scroll": scroll_timeout,
            "scroll_id": scroll_id
        }
        response = requests.post(f"{url}/_search/scroll", json=scroll_request, headers=headers, auth=auth)
        if response.status_code != 200:
            print("Failed to retrieve data from the URL:", response.status_code)
            break

        data = response.json()
        hits = data['hits']['hits']
        if not hits:
            break
        append_to_json(hits, filename)

def append_to_json(data, filename):
    with open(filename, 'a') as file:
        for hit in data:
            json.dump(hit, file)
            file.write('\n')

if __name__ == "__main__":
    url = 'http://distribution.virk.dk/cvr-permanent/virksomhed'
    username = 'SafeOdds_CVR_I_SKYEN'
    password = '7080bee8-7809-423e-9bd7-73d669f0cfde'

    query = {
        "query": {
            "match": {
                "Vrvirksomhed.beliggenhedsadresse.kommune.kommuneNavn": "SLAGELSE"
            }
        },
        "size": 1000  # Adjust the batch size as needed
    }

    filename = 'custom_filename.json'  # Specify the custom filename here
    retrieve_data_and_append_to_json(url, HTTPBasicAuth(username, password), query, filename)
