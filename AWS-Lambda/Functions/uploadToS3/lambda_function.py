import boto3
from dbc import DBC
import base64


def generate_file_path(username, imageType):

    if imageType == "ProfilePicture":

        filename = f"{username}_perfil.png"
        filepath = f"perfil/{username}_perfil.jpg"

    if imageType == "INEPicture":

        filename = f"{username}_ine.png"
        filepath = f"ine/{username}_ine.jpg"

    if imageType == "ComprobantePicture":

        filename = f"{username}_comprobante.png"
        filepath = f"comprobante/{username}_comprobante.jpg"

    if imageType == "CartaAntecedentesPicture":

        filename = f"{username}_cartaAntecedentes.png"
        filepath = f"cartaAntecedentes/{username}_cartaAntecedente.jpg"

    return filename, filepath

def update_registry(filepath, username, imageType):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    url = f"https://bancodetiempo.s3.amazonaws.com/{filepath}"

    if imageType == "ProfilePicture":
        query = f"UPDATE Usuario SET foto = \"{url}\" WHERE idUsuario = \"{username}\""

    if imageType == "INEPicture":
        query = f"UPDATE Documentos SET ine = \"{url}\" WHERE idUser = \"{username}\""

    if imageType == "ComprobantePicture":
        query = f"UPDATE Documentos SET comprobante = \"{url}\" WHERE idUser = \"{username}\""
    
    if imageType == "CartaAntecedentesPicture":
        query = f"UPDATE Documentos SET cartaAntecedentes = \"{url}\" WHERE idUser = \"{username}\""

    queryResult = dbHandler.SQL_execute_oneway_statement(query)

    dbHandler.SQL_stop()

    return url


def upload_image(image64, username, imageType):
    try:
        s3 = boto3.client('s3')
        bucket = "bancodetiempo"

        image64 = image64.encode("utf-8")
        imageBytes = base64.b64decode(image64)

        filename, filepath = generate_file_path(username, imageType)

        with open(f"/tmp/{filename}","wb") as img:
            img.write(imageBytes)
        
        with open(f"/tmp/{filename}","rb") as img:
            s3.upload_fileobj(img, bucket, filepath)
        # s3.put_object(Bucket = bucket, Key = filepath, Body = image)

        url = update_registry(filepath, username, imageType)
        
        if imageType == "ProfilePicture":

            data = {
                    "transactionApproval": 1,
                    "url": url
                    }
        else:
            data = {
                    "transactionApproval": 1
                    }

        return data
    except:
        data = {
                "transactionApproval": 0
                }
        return data



def lambda_handler(event, context):

    imageType = event["type"]
    image = event["image"]
    username = event["username"]

    data = upload_image(image, username, imageType)

    return data
