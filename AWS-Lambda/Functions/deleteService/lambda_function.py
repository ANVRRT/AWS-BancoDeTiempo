from dbc import DBC

def check_opened_services(dbHandler, idServicio):
    query = f"SELECT idServicio FROM Recibe WHERE idServicio = {idServicio} AND estado = \"OPEN\" "
    queryResult = dbHandler.SQL_execute_twoway_statement(query)
    
    if queryResult:
        return True
    return False

def delete_notification(dbHandler, idServicio):
    query = f"DELETE FROM Notificacion WHERE idServicio = {idServicio} "
    dbHandler.SQL_execute_oneway_statement(query)

def delete_recibe(dbHandler, idServicio):
    query = f"DELETE FROM Recibe WHERE idServicio = {idServicio} "
    dbHandler.SQL_execute_oneway_statement(query)

def delete_service(dbHandler, idServicio):
    query = f"DELETE FROM Servicios WHERE idServicio = {idServicio} "
    dbHandler.SQL_execute_oneway_statement(query)

def start_delete_service(idServicio):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    data = {
            "transactionApproval": 1,
    }

    openedService = check_opened_services(dbHandler, idServicio)
    if openedService:
        data["transactionApproval"] = 0
    else:
        delete_notification(dbHandler, idServicio)
        delete_recibe(dbHandler, idServicio)
        delete_service(dbHandler, idServicio)
    
    return data


def lambda_handler(event, context):

    idServicio = event["idServicio"]


    data = start_delete_service(idServicio)
    

    return data
