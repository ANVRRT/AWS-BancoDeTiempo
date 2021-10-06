import json
import boto3
from dbc import DBC
import base64


def upload_profile_image(image64,username):
    try:
        dbHandler = DBC()
        dbHandler.SQL_initialize()
        s3 = boto3.client('s3')

        bucket = "bancodetiempo"
        
        filename = f"{username}_perfil.png"
        filepath = f"perfil/{username}_perfil.jpg"

        image64 = image64.encode("utf-8")
        imageBytes = base64.b64decode(image64)

        with open(f"/tmp/{filename}","wb") as img:
            img.write(imageBytes)
        
        with open(f"/tmp/{filename}","rb") as img:
            s3.upload_fileobj(img, bucket, filepath)
        # s3.put_object(Bucket = bucket, Key = filepath, Body = image)


        url = f"https://bancodetiempo.s3.amazonaws.com/{filepath}"


        query = f"UPDATE Usuario SET foto = \"{url}\" WHERE idUsuario = \"{username}\""

        queryResult = dbHandler.SQL_execute_oneway_statement(query)

        dbHandler.SQL_stop()
        
        return 1;
    except:
        return 0;



def lambda_handler(event, context):

    imageType = event["type"]
    image = event["image"]
    username = event["username"]

    if imageType == "ProfilePicture":
        data = upload_profile_image(image,username)

    return data
