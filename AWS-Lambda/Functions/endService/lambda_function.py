from dbc import DBC

def activate_REQUEST_notifications(dbHandler, username, userType):
    if userType == "Emisor":
        query = f"UPDATE Notificacion SET estado = 1 WHERE idEmisor = \"{username}\" AND tipo = \"REQUEST\" "
    elif userType == "Receptor":
        query = f"UPDATE Notificacion SET estado = 1 WHERE idReceptor = \"{username}\" AND tipo = \"REQUEST\" "
    
    dbHandler.SQL_execute_oneway_statement(query)

def activate_services(dbHandler, username):
    query = f"UPDATE Servicios SET estado = 1 WHERE idUsuario = \"{username}\" "
    dbHandler.SQL_execute_oneway_statement(query)

def rate_service(dbHandler, idServicio, stars):

    query = f"UPDATE Servicios SET {stars} = {stars} + 1 WHERE idServicio = {idServicio} "
    dbHandler.SQL_execute_oneway_statement(query)

def change_notification_to_ended(dbHandler, idNot):

    query = f"UPDATE Notificacion SET tipo = \"ENDED\" WHERE idNotificacion = {idNot}"
    dbHandler.SQL_execute_oneway_statement(query)

def close_registry_service(dbHandler, idServicio):

    query = f"UPDATE Recibe SET estado = \"CLOSED\" WHERE estado = \"OPEN\" "
    dbHandler.SQL_execute_oneway_statement(query)

def end_service(data):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    activate_REQUEST_notifications(dbHandler, data["idReceptor"], "Receptor")
    activate_REQUEST_notifications(dbHandler, data["idEmisor"], "Emisor")

    activate_services(dbHandler, data["idReceptor"])
    activate_services(dbHandler, data["idEmisor"])


    rate_service(dbHandler, data["idServicio"], data["stars"])
    change_notification_to_ended(dbHandler, data["idNotificacion"])
    close_registry_service(dbHandler, data["idServicio"])

    response = {
                "transactionApproval": 1
                }
    return response
    

def lambda_handler(event, context):

    data = {
            "idServicio": event["idServicio"],
            "idReceptor" : event["idReceptor"],
            "idEmisor" : event["idEmisor"],
            "idNotificacion": event["idNotificacion"],
            "stars": event["stars"]
            }
    
    data = end_service(data)
    

    return data