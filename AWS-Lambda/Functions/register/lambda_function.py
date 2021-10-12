import json
import requests
from dbc import DBC

def error_processor(error, idUsuario,correo):
    errorList ={
                idUsuario: "Usuario duplicado",
                correo: "Correo duplicado",
                "None": ""
                }
    errorMessage = "Error not found in list"
    try:
        error.index(idUsuario)
        errorMessage = errorList[idUsuario]
        secondVerification = False
    except:
        secondVerification = True
    
    if secondVerification:
        try:
            error.index(correo)
            errorMessage = errorList[correo]
        except:
            errorMessage = errorList["None"]

    return errorMessage

def approve_register(data):
    
    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"""INSERT INTO Usuario VALUES(
                        \"{data['idUsuario']}\",
                        \"{data['nombre']}\",
                        \"{data['apellidoP']}\",
                        \"{data['apellidoM']}\",
                        \"{data['calle']}\",
                        \"{data['numero']}\",
                        \"{data['colonia']}\",
                        \"{data['municipio']}\",
                        \"{data['estado']}\",
                        \"{data['correo']}\",
                        {data['CPP']},
                        \"{data['contrasena']}\",
                        0,
                        "NULL",
                        0
                )   
                """

    query2 = f"""INSERT INTO Documentos VALUES(
                        \"{data['idUsuario']}\",
                        "NULL",
                        0,
                        "NULL",
                        0,
                        "NULL",
                        0
                )
                """

    queryResult, error = dbHandler.SQL_execute_oneway_statement(query)



    if not queryResult:
        error = error_processor(error, data['idUsuario'],data['correo'])
        data = {
            "registerApproval": 0,
            "error": error
            }
    else:
        queryResult2, error2 = dbHandler.SQL_execute_oneway_statement(query2)
        if not queryResult2:
            data = {
                "registerApproval": 0,
                "error": error2
                }
        else:
            data = {
                "registerApproval": 1,
                "error": ""
                }


    dbHandler.SQL_stop()
    
    
    

    
    return data
    
    #return 1

def lambda_handler(event, context):
    
    image = event["image"]

    data = approve_register(event)

    callAPI = "https://bka70s5pka.execute-api.us-east-1.amazonaws.com/API/uploadimage"
    dataPhoto = {
        "image": image,
        "type": "ProfilePicture",
        "username": event["idUsuario"]
    }
    response = requests.post(callAPI, json.dumps(dataPhoto))
    response = json.loads(response.content)
    transactionApproval = response["transactionApproval"]

    if not transactionApproval:
        data["registerApproval"] = 0
        data["error"] = "Error submiting image"


    return data