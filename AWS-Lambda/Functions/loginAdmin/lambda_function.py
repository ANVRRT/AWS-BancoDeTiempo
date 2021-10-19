import json
from dbc import DBC

def approve_login(user,password):
    
    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"SELECT * FROM Admin WHERE id = \"{user}\" AND contrasena = \"{password}\""

    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    dbHandler.SQL_stop()
    
    if not queryResult:

        approval = 0
    else:
        approval = 1

    data = {}

    data["loginApproval"] = approval


    return data



def lambda_handler(event, context):
    
    data = approve_login(event['username'],event['password'])
    return data
