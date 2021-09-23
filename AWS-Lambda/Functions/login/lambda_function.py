import json
from dbc import DBC
from hashlib import sha256

def approve_login(user,password):
    dbHandler = DBC()
    dbHandler.SQL_initialize()

    # password = password.encode()
    # password = sha256(password).hexdigest()

    query = f"SELECT idUsuario FROM Usuario WHERE idUsuario = \"{user}\" AND contrasena = \"{password}\""

    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    if queryResult:
        approval = 1
    else:
        approval = 0

    return approval

def lambda_handler(event, context):
    
    approval = approve_login(event['user'],event['password'])
    return {
        'loginApproval': approval

    }
