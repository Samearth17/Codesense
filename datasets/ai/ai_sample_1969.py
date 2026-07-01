import requests
import json

word = input("Enter a word: ")

url = "https://api.datamuse.com/words?rel_syn=" + word

response = requests.get(url)

if response.status_code == 200:
 json_data = json.loads(response.text)
 synonyms = [item['word'] for item in json_data]
 print(synonyms)
else:
 print("Something went wrong!")