import json
from dbc import DBC
from hashlib import sha256

def approve_login():
    
    dbHandler = DBC()
    dbHandler.SQL_initialize()
    
    query2 = f"SELECT idUser, nombre, apellidoP, ine, ine_approval, comprobante, comprobante_approval, cartaAntecedentes, cartaAntecedentes_approval, foto FROM Documentos INNER JOIN Usuario ON idUsuario = idUser WHERE documentos_approval = 0;"

    queryResult2 = dbHandler.SQL_execute_twoway_statement(query2)

    dbHandler.SQL_stop()

    data = {}

    for userData in queryResult2:
        data[userData[0]] = {
                            "id": userData[0],
                            "nombre": userData[1],
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
    
    data = approve_login()
    return data
