from dbc import DBC

def check_active_service(dbHandler ,username, userType):

    if userType == "Emisor":
        query = f"SELECT estado FROM Recibe WHERE idEmisor = \"{username}\" AND estado = \"OPEN\" "

    elif userType == "Receptor":
        query = f"SELECT estado FROM Recibe WHERE idReceptor = \"{username}\" AND estado = \"OPEN\" "

    queryResult = dbHandler.SQL_execute_twoway_statement(query)
    if queryResult:
        return True

    return False

def check_active_hours(dbHandler, username):

    query = f"SELECT estatusHoras FROM Usuario WHERE idUsuario = \"{username}\" AND estatusHoras = 1 "
    queryResult = dbHandler.SQL_execute_twoway_statement(query)
    
    if not queryResult:
        return False
    return True

def remove_active_hours(dbHandler, username):

    query = f"UPDATE Usuario SET estatusHoras = 0 WHERE idUsuario = \"{username}\""
    dbHandler.SQL_execute_oneway_statement(query)

def deactivate_REQUEST_notifications(dbHandler, username, userType):

    if userType == "Emisor":
        query = f"UPDATE Notificacion SET estado = 0 WHERE idEmisor = \"{username}\" AND tipo = \"REQUEST\" "
    elif userType == "Receptor":
        query = f"UPDATE Notificacion SET estado = 0 WHERE idReceptor = \"{username}\" AND tipo = \"REQUEST\" "
    
    dbHandler.SQL_execute_oneway_statement(query)

def deactivate_services(dbHandler, username):

    query = f"UPDATE Servicios SET estado = 0 WHERE idUsuario = \"{username}\" "
    dbHandler.SQL_execute_oneway_statement(query)

def activate_service(dbHandler, idReceptor, idEmisor, idServicio):
    query = f"""INSERT INTO Recibe VALUES(
            NULL,
            \"{idReceptor}\",
            \"{idServicio}\",
            \"{idEmisor}\",
            \"OPEN\"
            )
            """
    dbHandler.SQL_execute_oneway_statement(query)
    
# def update_notification_to_accepted(dbHandler, idNot):
#     query = f"UPDATE Notification SET tipo = \"ACCEPTED\" WHERE idNotificacion = {idNot}"
#     queryResult = dbHandler.SQL_execute_oneway_statement(query)


def preprocess_transaction(dbHandler, data):

    if data["tipo"] == "REQUEST":

        activeHours = check_active_hours(dbHandler,data["idReceptor"])
        if not activeHours:
            return False

        activeService = check_active_service(dbHandler, data['idEmisor'], "Emisor")
        if activeService:
            return False

    elif data["tipo"] == "ACCEPTED":


        #Check hours of the one that wants the service
        activeHours = check_active_hours(dbHandler,data["idReceptor"])
        if not activeHours:
            return False

        #Check if no service is currently going on the one that wants the service
        activeService = check_active_service(dbHandler, data['idReceptor'], "Receptor")
        if activeService:
            return False

        #Check if the one that is giving the service has no other currently going on services.
        activeService = check_active_service(dbHandler, data['idEmisor'], "Emisor")
        if activeService:
            return False


        #Delete hours of the one that wants the service
        remove_active_hours(dbHandler, data['idReceptor'])


        #Deactivate all REQUEST notifications of the one that wants the service
        deactivate_REQUEST_notifications(dbHandler, data['idReceptor'], "Receptor")

        #Deactivate all REQUEST notifications of the one that is giving the service
        deactivate_REQUEST_notifications(dbHandler, data['idEmisor'], "Emisor")


        #Deactivate all services of the one that that wants the service
        deactivate_services(dbHandler, data['idReceptor'])

        #Deactivate all services of the one that is giving the service 
        deactivate_services(dbHandler, data['idEmisor'])

        #Generate registry of Recibe table setting an "OPEN" service for the 2 actors.
        activate_service(dbHandler, data["idReceptor"], data["idEmisor"], data["idServicio"])

        #Update REQUEST notification to ACCEPTED and activate it again
        #It gets done in the main defined query
        

    return True

def define_query(data):

    if data["tipo"] == "REQUEST":
        query = f"""INSERT INTO Notificacion VALUES(
                    NULL,
                    \"{data["idEmisor"]}\",
                    \"{data["idReceptor"]}\",
                    {data["idServicio"]},
                    \"{data["tipo"]}\",
                    1
                    )
                    """
    else:
        query = f"UPDATE Notificacion SET tipo = \"{data['tipo']}\" WHERE idNotificacion = {data['idNot']}"

    return query



def process_notification(dataReceived):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    data = {
        "transactionApproval": 1
        }

    approval = preprocess_transaction(dbHandler, dataReceived)

    if approval:

        query = define_query(dataReceived)

        queryResult = dbHandler.SQL_execute_oneway_statement(query)

        if not queryResult:
            data["transactionApproval"] = 0
    else:

        data["transactionApproval"] = 0
        
    dbHandler.SQL_stop()
    
    return data

def lambda_handler(event, context):

    if event["type"] == "REQUEST":

        data = {
                "idServicio": event["idServicio"],
                "idEmisor": event["idEmisor"],
                "idReceptor": event["idReceptor"],
                "tipo": event["type"]
                }
                
    elif event["type"] == "ACCEPTED":

        data = {
                "idServicio": event["idServicio"],
                "idEmisor": event["idEmisor"],
                "idReceptor": event["idReceptor"],
                "tipo": event["type"],
                "idNot": event["idNot"]
                }
    else:

        data = {
                "tipo": event["type"],
                "idNot": event["idNot"]
                }

    
    data = process_notification(data)
    

    return data

"""
{
    "idServicio": lala,
    "idEmisor": ElQueDaElServicio,
    "idReceptor": ElQueQuiereElServicio,
    "type": REQUEST, ACCEPTED, REJECTED

}

# REQUEST //QUIERE TU SERVICIO
    Funciones:
        Aceptar
        Negar
# ACCEPTED //ACEPTO DARTE EL SERVICIO
    Funciones:
        Ponte en contacto
        Terminar servicio //NO FINALIZAR SERVICIO HASTA HABERLO OTORGADO
            Calificar servicio
# REJECTED //NO QUIERE DARTE EL SERVICIO
    Funciones:
        Ninguna

# ENDED //SERVICIOS FINALIZADOS
    Funciones:
        Ninguna


"""