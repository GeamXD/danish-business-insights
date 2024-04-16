import json

with open('data.json', 'r') as f:
    data = json.load(f)


hits = data['hits']['hits']
print(len(hits))