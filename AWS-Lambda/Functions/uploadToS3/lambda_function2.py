import json
import boto3
import base64


def upload_image(image,username):
    try:
        s3 = boto3.client('s3')

        bucket = "bancodetiempo"    

        image = image[image.find(",")+1:]
        
        image = base64.b64decode(image +  "===")
                    

        filename = f"{username}_ine.png"

        s3.put_object(Bucket = bucket, Key = filename, Body = image)

        return 1
    except:
        return 0

def lambda_handler(event, context):
    """
    {
        "username": "chanito"
        "image": imagen
        
    }
    
    """
    image = event["image"].encode()
    username = event["username"]


    data = upload_image(image,username)

    return data
