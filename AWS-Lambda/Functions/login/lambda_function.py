import json
from dbc import DBC
from hashlib import sha256

def approve_login(user,password):
    
    dbHandler = DBC()
    dbHandler.SQL_initialize()

    # password = password.encode()
    # password = sha256(password).hexdigest()

    query = f"SELECT * FROM Usuario WHERE idUsuario = \"{user}\" AND contrasena = \"{password}\""

    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    dbHandler.SQL_stop()

    if queryResult:
        queryResult = queryResult[0]
        if queryResult[15]:
            approval = 1
            data = {
                'loginApproval': approval,
                'username': queryResult[0],
                'name': queryResult[1],
                'lastName': queryResult[2],
                'email': queryResult[9],
                'statusHours': queryResult[12],
                'documentosApproval': queryResult[14],
                'foto': queryResult[13],
                'colonia': queryResult[6],
                "lastNameM": queryResult[3],
                "calle": queryResult[4],
                "numero": queryResult[5],
                "municipio": queryResult[7],
                "estado": queryResult[8],
                "CP": queryResult[10]
                }
        else:
            data = {
                    'loginApproval': 0
                    }
    else:
        approval = 0
        data = {
            'loginApproval': approval
            }
    
    return data

def lambda_handler(event, context):
    
    data = approve_login(event['username'],event['password'])
    return data
