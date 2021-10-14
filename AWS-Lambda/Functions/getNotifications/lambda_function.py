from dbc import DBC

def getNotifications(username):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"""SELECT idNotificacion, idEmisor, idReceptor, idServicio, tipo, nombre, descripcion FROM Notificacion INNER JOIN Servicios 
                    ON Servicios.idServicio = Notificacion.idServicio 
                    WHERE (idEmisor = \"{username}\" AND tipo = \"REQUEST\") AND estado = 1

                    UNION

                SELECT idNotificacion, idEmisor, idReceptor, idServicio, tipo, nombre, descripcion FROM Notificacion INNER JOIN Servicios 
                    ON Servicios.idServicio = Notificacion.idServicio 
                    WHERE (idReceptor = \"{username}\" AND (tipo = \"ACCEPTED\" OR tipo = \"REJECTED\") ) AND estado = 1
                    """

    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    data = {"notificaciones": []}

    for service in queryResult:
        
        data["notificaciones"].append({
                    "idNot": service[0],
                    "idEmisor": service[1],
                    "idReceptor": service[2],
                    "idServicio": service[3],
                    "tipo": service[4],
                    "nombre": service[5],
                    "descripcion": service[6]
                    })
                    
    dbHandler.SQL_stop()

    return data

def lambda_handler(event, context):

    username = event["username"]

    


    data = getNotifications(username)
    

    return data