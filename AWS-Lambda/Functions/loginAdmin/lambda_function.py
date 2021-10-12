import json
from dbc import DBC
from hashlib import sha256

def approve_login(user,password):
    
    dbHandler = DBC()
    dbHandler.SQL_initialize()

    # password = password.encode()
    # password = sha256(password).hexdigest()

    query = f"SELECT * FROM Admin WHERE id = \"{user}\" AND contrasena = \"{password}\""

    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    if not queryResult:

        approval = 0
        data = {
            'loginApproval': approval
            }
    
        return data
    
    query2 = f"SELECT idUser, nombre, apellidoP, ine, ine_approval, comprobante, comprobante_approval, cartaAntecedentes, cartaAntecedentes_approval, foto FROM Documentos INNER JOIN Usuario ON idUsuario = idUser;"

    queryResult2 = dbHandler.SQL_execute_twoway_statement(query2)

    dbHandler.SQL_stop()

    data = {}

    data["loginApproval"] = 1

    for userData in queryResult2:
        data[userData[0]] = {
                            "id": userData[0],
                            "nombre:": userData[1],
                            "apellido": userData[2],
                            "ine": userData[3],
                            "ine_approval": userData[4],
                            "comprobante": userData[5],
                            "comprobante_approval": userData[6],
                            "cartaAntecedentes": userData[7],
                            "cartaAntecedentes_approval": userData[8],
                            "foto": userData[9]
                            }
    return data



def lambda_handler(event, context):
    
    data = approve_login(event['username'],event['password'])
    return data
