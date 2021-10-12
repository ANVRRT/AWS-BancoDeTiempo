import boto3
from dbc import DBC

def get_user_services(username):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"SELECT * FROM Servicios WHERE idUsuario = \"{username}\" AND estado = 1"

    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    data = {"ofertas": []}

    for service in queryResult:
        
        data["ofertas"].append({
                    "idServicio": service[0],
                    "idUsuario": service[1],
                    "colonia": service[2],
                    "nombre": service[4],
                    "descripcion": service[5],
                    "certificado": service[7],
                    "imagen": service[8]
                    })

    return data

def lambda_handler(event, context):

    username = event["username"]

    data = get_user_services(username)
    

    return data
