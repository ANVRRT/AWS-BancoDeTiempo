import json
from dbc import DBC
import boto3
import base64


def generate_file_path(imageType, idServicio):

    if imageType == "PresentationImage":

        filename = f"{idServicio}.png"
        filepath = f"imagenServicio/{idServicio}.png"
    

    if imageType == "Certification":

        filename = f"{idServicio}.png"
        filepath = f"certificacion/{idServicio}.png"

    return filename, filepath

def process_image(imageType, image64, idServicio):

    s3 = boto3.client('s3')
    bucket = "bancodetiemposervicios"

    image64 = image64.encode("utf-8")
    imageBytes = base64.b64decode(image64)

    filename, filepath = generate_file_path(imageType, idServicio)

    with open(f"/tmp/{filename}","wb") as img:
        img.write(imageBytes)
    
    with open(f"/tmp/{filename}","rb") as img:
        s3.upload_fileobj(img, bucket, filepath)

    url = f"https://bancodetiemposervicios.s3.amazonaws.com/{filepath}"

    return url


def generate_servicios_row(data, dbHandler):

    query = f"""INSERT INTO Servicios VALUES(
                    NULL,
                    \"{data['username']}\",
                    \"{data['colonia']}\",
                    \"{data['category']}\",
                    \"{data['name']}\",
                    \"{data['description']}\",
                    1,
                    \"NULL\",
                    \"NULL\",
                    0,
                    0,
                    0,
                    0,
                    0,
                    0                  
            )
    """
    queryResult = dbHandler.SQL_execute_oneway_statement(query)
    if not queryResult:
        return False

    query2 = f"SELECT idServicio FROM Servicios WHERE nombre = \"{data['name']}\" AND  idUsuario = \"{data['username']}\" "
    queryResult2 = dbHandler.SQL_execute_twoway_statement(query2)
    if not queryResult2:
        return False
    else:
        queryResult2 = queryResult2[0][0]

    return queryResult2

def update_servicios_row(dbHandler, idServicio, imageURL, certificationURL):

    query = f"UPDATE Servicios SET image = \"{imageURL}\" WHERE idServicio = \"{idServicio}\""
    queryResult = dbHandler.SQL_execute_oneway_statement(query)

    if not queryResult:
        return False

    query2 = f"UPDATE Servicios SET certificado = \"{certificationURL}\" WHERE idServicio = \"{idServicio}\""
    queryResult2 = dbHandler.SQL_execute_oneway_statement(query)

    if not queryResult2:
        return False
    
    return True
    
def create_service(data):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    response = {
        "transactionApproval": 0
        }

    idServicio = generate_servicios_row(data, dbHandler)
    
    if not idServicio:
        return response
    else:
        data["idServicio"] = idServicio

    imageServiceURL = process_image("PresentationImage", data["imageService"], idServicio)

    if data["certification"] != "NULL":
        certificationURL = process_image("Certification", data["certification"], idServicio)
    else:
        certificationURL = "NULL"

    approval = update_servicios_row(dbHandler, idServicio, imageServiceURL, certificationURL)

    if not approval:
        return response
    else:
        response["transactionApproval"] = 1
        
    dbHandler.SQL_stop()

    return response


def lambda_handler(event, context):
    username = event["username"]
    category = event["categoria"]
    name = event["nombre"]
    description = event["descripcion"]

    imageService = event["image"]
    certification = event["certificado"]

    colonia = event["colonia"]



    data = {
        "username": username,
        "category": category,
        "name": name,
        "description": description,
        "colonia": colonia,
        "imageService":imageService,
        "certification": certification
    }

    response = create_service(data)

    return response
