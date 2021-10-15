from dbc import DBC

def getNotifications(username):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"""SELECT idNotificacion, idReceptor, idEmisor, Notificacion.idServicio, image, nombre, categoria, descripcion FROM Notificacion INNER JOIN Servicios 
                    ON Servicios.idServicio = Notificacion.idServicio 
                    WHERE (idReceptor = \"{username}\" AND tipo = \"ACCEPTED\") AND Notificacion.estado = 1
                    """

    queryResult = dbHandler.SQL_execute_twoway_statement(query)

    if queryResult:
        service = queryResult[0]

        data = {
                "idNot": service[0],
                "idReceptor": service[1],
                "idEmisor": service[2],
                "idServicio": service[3],
                "image": service[4],
                "nombre": service[5],
                "categoria": service[6],
                "descripcion": service[7],
                "something": 1
                }
    else:
        data = {
                "something": 0
            }
    # data = {"notificaciones": []}

    # for service in queryResult:
        
    #     data["notificaciones"].append({
    #                 "idNot": service[0],
    #                 "idReceptor": service[1],
    #                 "idEmisor": service[2],
    #                 "idServicio": service[3],
    #                 "image": service[4],
    #                 "nombre": service[5],
    #                 "categoria": service[6],
    #                 "descripcion": service[7]
    #                 })
                    
    dbHandler.SQL_stop()

    return data

def lambda_handler(event, context):

    username = event["username"]

    


    data = getNotifications(username)
    

    return data