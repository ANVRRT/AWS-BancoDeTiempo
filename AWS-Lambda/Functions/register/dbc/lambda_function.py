import json
from dbc import DBC

def error_processor(error, idUsuario,correo):
    errorList ={
                idUsuario: "Usuario duplicado",
                correo: "Correo duplicado",
                "None": ""
                }
    errorMessage = "Error not found in list"
    print(error)
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
                        1,
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

    data = approve_register(event)
    return data

if __name__ == "__main__":
    data = {
        "idUsuario": "Marco",
        "nombre": "Marco",
        "apellidoP": "Almazan",
        "apellidoM": "Martínez",
        "calle": "Nose",
        "numero": "1",
        "colonia": "ColoniaX",
        "municipio": "MunicipioX",
        "estado": "EstadoX",
        "correo": "CorreoX@gmail.com",
        "CPP": 50963,
        "contrasena": "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"
        }
    data2 = approve_register(data)
    print(data2)