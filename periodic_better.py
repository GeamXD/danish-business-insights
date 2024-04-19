import requests
import schedule
import time
import json

# Define the URL and authentication credentials

# Define the query
query = {
    "size": 2000,
    "query": {
        "match_all": {}
    }
}

# Additional headers
headers = {
    'Content-Type': 'application/json',
}

def make_request():
    url = 'http://distribution.virk.dk/offentliggoerelser/_search'
    username = 'SafeOdds_CVR_I_SKYEN'
    password = '7080bee8-7809-423e-9bd7-73d669f0cfde'

    # Send POST request with basic authentication
    response = requests.post(url, auth=(username, password), headers=headers, json=query)

    # Check if request was successful
    if response.status_code == 200:
        # Save response data to a file
        with open('response_data2_new.json', 'w') as file:
            file.write(response.text)
        
        # Load the JSON data
        with open('response_data2_new.json') as f:
            data = json.load(f)
        
        # Extract the hits
        hits = data['hits']['hits']
        
        # Find all hits with XML documents
        xml_hits = [hit for hit in hits if any(dokument['dokumentMimeType'] == 'application/xml' for dokument in hit['_source']['dokumenter'])]
        
        # Extract the dokumentUrl for all XML documents
        xml_dokument_urls = [dokument['dokumentUrl'] for hit in xml_hits for dokument in hit['_source']['dokumenter'] if dokument['dokumentMimeType'] == 'application/xml']
        
        # Save the URLs to a text file
        with open('xml_urls_testing.txt', 'a') as f:
            for url in xml_dokument_urls:
                f.write("%s\n" % url)
        
        print("Data saved to response_data.json")
        print("XML URLs saved to xml_urls.txt")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Schedule the request to run every 60 seconds
schedule.every(5).seconds.do(make_request)

while True:
    schedule.run_pending()
    time.sleep(1)