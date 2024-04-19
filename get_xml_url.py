import json

# Load the JSON data
with open('response_data.json') as f:
    data = json.load(f)

# Extract the hits
hits = data['hits']['hits']

# Find all hits with XML documents
xml_hits = [hit for hit in hits if any(dokument['dokumentMimeType'] == 'application/xml' for dokument in hit['_source']['dokumenter'])]

# Extract the dokumentUrl for all XML documents
xml_dokument_urls = [dokument['dokumentUrl'] for hit in xml_hits for dokument in hit['_source']['dokumenter'] if dokument['dokumentMimeType'] == 'application/xml']

# Save the URLs to a text file
with open('xml_urls_2.txt', 'w') as f:
    for url in xml_dokument_urls:
        f.write("%s\n" % url)