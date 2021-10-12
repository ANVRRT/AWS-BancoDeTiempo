import json
from dbc import DBC


def define_query(type,username):
    query = ""
    if type == "INE":
        query = f"UPDATE Documentos SET ine_approval = 1 WHERE idUser = \"{username}\""
    
    if type == "Comprobante":
        query = f"UPDATE Documentos SET comprobante_approval = 1 WHERE idUser = \"{username}\""

    if type == "Carta":
        query = f"UPDATE Documentos SET cartaAntecedentes_approval = 1 WHERE idUser = \"{username}\""

    return query

def approve_all(dbHandler, username):
    query = f"UPDATE Documentos SET ine_approval = 1, comprobante_approval = 1, cartaAntecedentes_approval = 1 WHERE idUser = \"{username}\""
    queryResult = dbHandler.SQL_execute_oneway_statement(query)
    if not queryResult:
        return False

    query2 = f"UPDATE Usuario SET documentos_approval = 1, estatusHoras = 1 WHERE idUsuario = \"{username}\""
    queryResult2 = dbHandler.SQL_execute_oneway_statement(query2)
    if not queryResult2:
        return False

    return True


def lambda_handler(event, context):
    """
    "All"
    "INE"
    "Comprobante"
    "Carta"

    """
    username = event['queryStringParameters']['username']
    type = event['queryStringParameters']['type']

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    if type == "All":
        approval = approve_all(dbHandler, username)
        if approval:
            approval = 1
        else:
            approval = 0

    else:
        query = define_query(type, username)
        queryResult = dbHandler.SQL_execute_oneway_statement(query)
        if not queryResult:
            approval = 0
        else:
            approval = 1

    transaction = {}
    
    transaction["transactionApproval"] = approval    
    
    data = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
        'body': json.dumps(transaction)
    }
    dbHandler.SQL_stop()

    return data