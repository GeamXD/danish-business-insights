import json
import requests
import time
from datetime import datetime
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
    append_to_json(response.json()['hits']['hits'], filename)

    # Continue retrieving batches using scroll API
    while scroll_id:
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
        scroll_id = data.get("_scroll_id")

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
        "size": 3000  # Adjust the batch size as needed
    }

    # Define the number of times to run the script
    num_runs = 50
    # Define the sleep interval between each run (in seconds)
    sleep_interval = 20  # 1 minute

    for i in range(num_runs):
        print(f"Run {i+1}/{num_runs}")
        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"py_data_{timestamp}.json"
        retrieve_data_and_append_to_json(url, HTTPBasicAuth(username, password), query, filename)
        if i < num_runs - 1:
            print(f"Sleeping for {sleep_interval} seconds...")
            time.sleep(sleep_interval)
