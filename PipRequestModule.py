import requests
import json
import pyttsx3
response = requests.get("https://official-joke-api.appspot.com/random_ten")

response_status_code = response.status_code
response_text = response.text
jsonData = json.loads(response_text)


for data in jsonData:
   print(data)