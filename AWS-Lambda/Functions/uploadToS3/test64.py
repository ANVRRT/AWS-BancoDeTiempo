import requests
import json
import base64

with open('Anverso.jpeg','rb') as image:
    imageRead = image.read()
    imageBytes = imageRead

imageBase64 = base64.b64encode(imageBytes)

imageBase64String = imageBase64.decode("utf-8")


callAPI = "https://bka70s5pka.execute-api.us-east-1.amazonaws.com/API/uploadimage"
data = {
    "type": "ProfilePicture",
    "username": "alberto_123",
    "image": imageBase64String

}
response = requests.post(callAPI, json.dumps(data))
resp = json.loads(response.content)
response = resp
print(response)