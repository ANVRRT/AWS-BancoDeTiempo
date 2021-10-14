import boto3
from dbc import DBC

def get_user_services(username):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"SELECT idServicio, Servicios.idUsuario, colonia, Servicios.nombre, descripcion, certificado, image, Usuario.nombre as nombreU, Usuario.apellidoP, foto FROM Servicios LEFT JOIN Usuario ON Servicios.idUsuario = Usuario.idUsuario WHERE Servicios.idUsuario = \"{username}\" AND Servicios.estado = 1"

    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    data = {"ofertas": []}

    for service in queryResult:
        
        data["ofertas"].append({
                    "idServicio": service[0],
                    "idUsuario": service[1],
                    "colonia": service[2],
                    "nombre": service[3],
                    "descripcion": service[4],
                    "certificado": service[5],
                    "imagen": service[6],
                    "nombreUsuario": service[7],
                    "apellidoUsuario": service[8],
                    "foto": service[9]
                    })
    dbHandler.SQL_stop()

    return data

def lambda_handler(event, context):

    username = event["username"]

    data = get_user_services(username)
    

    return data
