import json

import requests
from icecream import ic
from get_credentials import Credentials

api_key2 = Credentials().merriam_webster_2




# The word you want to look up
word = 'dealt'


# The API endpoint URL
url = f'https://dictionaryapi.com/api/v3/references/learners/json/{word}?key={api_key2}'


# Make the API request
response = requests.get(url)

# Check if the request was successful
# if response.status_code == 200:
    # try:
        # Parse the JSON response

data = response.json()
# print(data)
json_string = json.dumps(data, indent=4)
# print(json_string)

# print(data[1].keys())
# print(data[1]['def'])
# print((len(data[1]['def'])))
# ic(data[1]['def'][0]['sseq'])
ic(len(data[1]['def'][0]['sseq']))
for _ in data[1]['def'][0]['sseq']:
    print(_)
# print(data[1]['meta']['stems'])
# print(data[1]['meta']['app-shortdef']['hw'])
# print(data[1]['meta']['app-shortdef']['fl'])
# for definition in data[1]['meta']['app-shortdef']['def']:
#
#     print(definition)



#     except (KeyError, IndexError, requests.exceptions.JSONDecodeError) as e:
#         print(f"Error: {type(e).__name__} - {e}")
# else:
#     print(f"Error: {response.status_code} - {response.text}")



