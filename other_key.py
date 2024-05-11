import requests
import json
import icecream as ic

from get_credentials import Credentials

api_key1 = Credentials().merriam_webster_1


# The word you want to look up
word = 'dealt'

# The API endpoint URL

url = f'https://dictionaryapi.com/api/v3/references/sd3/json/{word}?key={api_key1}'

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Parse the JSON response

        data = response.json()

        json_string = json.dumps(data, indent=4)
        print(json_string)



    except (KeyError, IndexError, requests.exceptions.JSONDecodeError) as e:
        print(f"Error: {type(e).__name__} - {e}")
else:
    print(f"Error: {response.status_code} - {response.text}")
