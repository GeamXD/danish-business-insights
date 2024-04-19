import requests
import schedule
import time

# Define the URL and authentication credentials
url = '(link unavailable)'
username = 'SafeOdds_CVR_I_SKYEN'
password = '7080bee8-7809-423e-9bd7-73d669f0cfde'

# Define the query
query = {
    "size": 2999,
    "query": {
        "match_all": {}
    }
}

# Additional headers
headers = {
    'Content-Type': 'application/json',
}

def make_request():
    # Send POST request with basic authentication
    response = requests.post(url, auth=(username, password), headers=headers, json=query)

    # Check if request was successful
    if response.status_code == 200:
        # Save response data to a file
        with open('response_data2_new.json', 'w') as file:
            file.write(response.text)
        print("Data saved to response_data.json")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Schedule the request to run every 60 seconds
schedule.every(60).seconds.do(make_request)

while True:
    schedule.run_pending()
    time.sleep(1)