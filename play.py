import json
import pprint

with open('slagelse_data.json', 'r') as f:
    data = json.load(f)


hits = data['hits']['hits']
print(len(hits))