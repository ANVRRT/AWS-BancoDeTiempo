import json
from dbc import DBC

def check_active_service(dbHandler ,username):
    query = f"SELECT estado FROM Recibe WHERE idEmisor = \"{username}\" AND estado = \"OPEN\" UNION SELECT estado FROM Recibe WHERE idReceptor = \"{username}\" AND estado = \"OPEN\"  "

    queryResult = dbHandler.SQL_execute_twoway_statement(query)
    if queryResult:
        return True
    return False

def deactivate_services(dbHandler, username):
    query = f"UPDATE Servicios SET estado = 0 WHERE idUsuario = \"{username}\" "
    dbHandler.SQL_execute_oneway_statement(query)

def remove_active_hours(dbHandler, username):
    query = f"UPDATE Usuario SET estatusHoras = 0 WHERE idUsuario = \"{username}\""
    dbHandler.SQL_execute_oneway_statement(query)

def deactivate_documents(dbHandler, username):
    query = f"UPDATE Usuario SET documentos_approval = 0 WHERE idUsuario = \"{username}\""
    dbHandler.SQL_execute_oneway_statement(query)

    query2 = f"UPDATE Documentos SET ine_approval = 0, comprobante_approval = 0, cartaAntecedentes_approval = 0 WHERE idUser = \"{username}\""
    dbHandler.SQL_execute_oneway_statement(query2)

def make_update(dbHandler, data):
    query = f"UPDATE Usuario SET nombre = \"{data['nombre']}\", apellidoP = \"{data['apellidoP']}\", apellidoM = \"{data['apellidoM']}\", calle = \"{data['calle']}\", numero = \"{data['numero']}\", CPP = {data['CP']}, colonia = \"{data['colonia']}\", municipio = \"{data['municipio']}\", estado = \"{data['estado']}\" WHERE idUsuario = \"{data['idUsuario']}\""
    dbHandler.SQL_execute_oneway_statement(query)


def update_user(data):
    dbHandler = DBC()
    dbHandler.SQL_initialize()

    activeService = check_active_service(dbHandler, data["idUsuario"])
    if activeService:
        response = {
                    "transactionApproval": 0,
                    "error": "No puedes actualizar tus datos mientras tienes un servicio activo."
                    }
        return response
    
    deactivate_services(dbHandler, data["idUsuario"])
    remove_active_hours(dbHandler, data["idUsuario"])
    deactivate_documents(dbHandler, data["idUsuario"])

    make_update(dbHandler, data)

    response = {
                "transactionApproval": 1,
                "error": ""
                }
    return response

def lambda_handler(event, context):



    data = update_user(event)
    # TODO implement
    return data

