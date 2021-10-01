import json
import boto3
import base64


def upload_image(image64,username):
    try:
        s3 = boto3.client('s3')

        bucket = "bancodetiempo"
        
        filename = f"{username}_INE.png"
        filepath = f"ine/{username}_INE.jpg"

        image = bytes.fromhex(image64)

        with open(f"/tmp/{filename}","wb") as img:
            img.write(image)
        
        with open(f"/tmp/{filename}","rb") as img:
            s3.upload_fileobj(img, bucket, filepath)
        # s3.put_object(Bucket = bucket, Key = filepath, Body = image)
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
    image = event["image"]
    username = event["username"]


    data = upload_image(image,username)

    return data
