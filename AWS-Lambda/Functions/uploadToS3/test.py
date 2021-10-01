import requests
import json
import base64

with open('Anverso.jpeg','rb') as image:
    imageRead = image.read()
    image64 = imageRead

print(type(image64))

callAPI = "https://bka70s5pka.execute-api.us-east-1.amazonaws.com/API/uploadimage"
data = {
    "username": "anvrrt",
    "image": image64.hex()

}
response = requests.post(callAPI, json.dumps(data))
resp = json.loads(response.content)
response = resp
print(response)