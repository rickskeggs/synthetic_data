import requests
#import response
import json
import pandas as pd

base_url = 'https://random-data-api.com/api/v2/'
size = 100
#response_type=json



url = '{}/beers?size={}&response_type=json'.format(base_url, size)

reply = requests.get(url)

reply.json()

#brand [name alcohol]

data = json.dumps(reply.json())
df = pd.DataFrame(columns=['brand','desc'])
for x in range(len(reply.json())):
    df['brand'].append(reply.json()[x]['brand'] )
    df['desc'].iloc[x] = [reply.json()[x]['name'] ,    df.append(reply.json()[x]['alcohol']) ]

print(df)


