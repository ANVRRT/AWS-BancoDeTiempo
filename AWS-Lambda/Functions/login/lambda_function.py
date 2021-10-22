import json
from dbc import DBC
from hashlib import sha256

def get_stars(dbHandler, username):
    query = f"SELECT V0, V1, V2, V3, V4, V5 FROM Servicios WHERE idUsuario = \"{username}\" "

    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    total = 0
    preAverage = 0

    for result in queryResult:
        total += 1
        totalService = result[0] + result[1] + result[2] + result[3] + result[4] + result[5]
        preAverageService = result[0] + result[1] + result[2] * 2 + result[3] * 3 + result[4] * 4 + result[5] * 5
        averageService = preAverageService / totalService

        preAverage += averageService
    if total != 0:
        average = preAverage / total
    else:
        average = 0

    return str(average)


def approve_login(user,password):
    
    dbHandler = DBC()
    dbHandler.SQL_initialize()

    # password = password.encode()
    # password = sha256(password).hexdigest()

    query = f"SELECT * FROM Usuario WHERE idUsuario = \"{user}\" AND contrasena = \"{password}\""

    queryResult = dbHandler.SQL_execute_twoway_statement(query)



    if queryResult:
        queryResult = queryResult[0]
        if queryResult[15]:

            stars = get_stars(dbHandler, queryResult[0])

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
                "CP": queryResult[10],
                "stars": stars
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

    dbHandler.SQL_stop()
    return data

def lambda_handler(event, context):
    
    data = approve_login(event['username'],event['password'])
    return data
