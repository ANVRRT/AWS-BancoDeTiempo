import boto3
from dbc import DBC

def get_services(colonia, category):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"SELECT * FROM Servicios WHERE ubicacion = \"{colonia}\" AND categoria = \"{category}\" AND estado = 1 "

    # query = f"SELECT * FROM Recibe LEFT JOIN Servicios ON ubicacion = \"{colonia}\" AND estado = \"OPEN\" "
    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    # data = query
    data = {}

    for service in queryResult:
        data[service[0]] = {
                    "idServicio": service[0],
                    "idUsuario": service[1],
                    "colonia": service[2],
                    "nombre": service[4],
                    "descripcion": service[5],
                    "certificado": service[7],
                    "imagen": service[8]
                    }

    return data

def lambda_handler(event, context):

    colonia = event["colonia"]
    category = event["categoria"]

    data = get_services(colonia, category)
    

    return data
