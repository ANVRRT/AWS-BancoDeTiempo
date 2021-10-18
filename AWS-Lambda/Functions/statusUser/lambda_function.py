from dbc import DBC


def verify_hours(dbHandler, username):

    query = f"SELECT estatusHoras FROM Usuario WHERE idUsuario = \"{username}\" "
    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    if queryResult:
        statusHoras = queryResult[0][0]

    return statusHoras

def verify_documents(dbHandler, username):

    query = f"SELECT documentos_approval FROM Usuario WHERE idUsuario = \"{username}\" "
    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    if queryResult:
        statusHoras = queryResult[0][0]

    return statusHoras


def lambda_handler(event, context):


    username = event["username"]
    type = event["type"]

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    data = {}

    if type == "horas":
        confirmation = verify_hours(dbHandler, username)

        data["statusHoras"] = confirmation
    
    if type == "documentos":
        confirmation = verify_documents(dbHandler, username)

        data["statusDocumentos"] = confirmation



    # TODO implement
    return data
