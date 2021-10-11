import boto3
from dbc import DBC

def generatePreQuery(colonias, categoria):
    preQuery = ""

    for colonia in colonias:
        preSecQuery = f"ubicacion = \"{colonia}\" OR "
        preQuery += preSecQuery

    preQuery = preQuery[:-3]
    preQuery += f"AND categoria = \"{categoria}\" AND estado = 1"

    return preQuery


def get_services(colonias, category):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    preQuery = generatePreQuery(colonias, category)

    query = f"SELECT * FROM Servicios WHERE {preQuery}"

    # query = f"SELECT * FROM Recibe LEFT JOIN Servicios ON ubicacion = \"{colonia}\" AND estado = \"OPEN\" "
    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    # data = query
    data = {}

    for service in queryResult:
        # data[service[0]] = {
        #                     "idCita": service[0],
        #                     "idReceptor": service[1],
        #                     "idServicio": service[2],
        #                     "idEmisor": service[3],
        #                     "comentario": service[5],
        #                     }
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

    colonias = event["colonia"]
    category = event["categoria"]
    coloniasArray = []

    for colonia in colonias.keys():
        coloniasArray.append(colonia)

    data = get_services(coloniasArray, category)
    

    return data
