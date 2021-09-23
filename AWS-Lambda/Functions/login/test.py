import requests
import json

callAPI = "https://bka70s5pka.execute-api.us-east-1.amazonaws.com/beta"
data = {
    "name": "Carlos"
}
response = requests.post(callAPI, json.dumps(data))
resp = json.loads(response.content)
response = resp["response"]
print(response)