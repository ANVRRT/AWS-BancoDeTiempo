import requests
import json

callAPI = "https://bka70s5pka.execute-api.us-east-1.amazonaws.com/API/getnotifications"
data = {
    "username": "Marco"
}
response = requests.post(callAPI, json.dumps(data))
resp = json.loads(response.content)
# response = resp["response"]
print(resp)