import json
import pandas as pd

with open('/workspaces/danish-business-insights/scrapping/business-data/ten_business.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
print(df.head())