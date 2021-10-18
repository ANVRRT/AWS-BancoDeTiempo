import requests
import json

callAPI = "https://bka70s5pka.execute-api.us-east-1.amazonaws.com/API/approveuserdocuments?username=test&type=pepelepe"
data = {
    "id": "test3",
    "type": "pep"
}
response = requests.get(callAPI)
resp = json.loads(response.content)
response = resp
print(response)