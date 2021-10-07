import boto3
from dbc import DBC

def get_services(colonia):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"SELECT * FROM Recibe LEFT JOIN Servicios ON ubicacion = \"{colonia}\" AND estado = \"OPEN\" "
    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    data = {}

    for service in queryResult:
        data[service[0]] = {
                            "idCita": service[0],
                            "idReceptor": service[1],
                            "idServicio": service[2],
                            "idEmisor": service[3],
                            "comentario": service[5],
                            }

    """
    data = {
        "1": {
            "idCita": service[0],
                            "idReceptor": service[1],
                            "idServicio": service[2],
                            "idEmisor": service[3],
                            "comentario": service[5],
        },
        "2": {
            "idCita": service[0],
                            "idReceptor": service[1],
                            "idServicio": service[2],
                            "idEmisor": service[3],
                            "comentario": service[5],
        }


    }
    
    """

    return data

def lambda_handler(event, context):

    colonia = event["colonia"]


    data = get_services(colonia)

    return data
