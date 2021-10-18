from dbc import DBC

def getNotifications(username):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = f"""SELECT idNotificacion, idEmisor, idReceptor, Notificacion.idServicio, tipo, nombre, descripcion FROM Notificacion INNER JOIN Servicios 
                    ON Servicios.idServicio = Notificacion.idServicio 
                    WHERE (idEmisor = \"{username}\" AND tipo = \"REQUEST\") AND Notificacion.estado = 1

                    UNION

                SELECT idNotificacion, idEmisor, idReceptor, Notificacion.idServicio, tipo, nombre, descripcion FROM Notificacion INNER JOIN Servicios 
                    ON Servicios.idServicio = Notificacion.idServicio 
                    WHERE (idReceptor = \"{username}\" AND tipo = "REJECTED\" ) AND Notificacion.estado = 1
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

    query2 = f"""SELECT idNotificacion, idEmisor, idReceptor, Notificacion.idServicio, tipo, nombre, descripcion FROM Notificacion INNER JOIN Servicios 
                    ON Servicios.idServicio = Notificacion.idServicio 
                    WHERE (idReceptor = \"{username}\" AND tipo = \"REQUEST\")  AND Notificacion.estado = 1
            """
    queryResult2 = dbHandler.SQL_execute_twoway_statement(query2)

    for service in queryResult2:
        
        data["notificaciones"].append({
                    "idNot": service[0],
                    "idEmisor": service[1],
                    "idReceptor": service[2],
                    "idServicio": service[3],
                    "tipo": "WAITING",
                    "nombre": service[5],
                    "descripcion": service[6]
                    })
    query3 = f"""SELECT idNotificacion, idEmisor, idReceptor, Notificacion.idServicio, tipo, Servicios.nombre, descripcion, Usuario.nombre, apellidoP, apellidoM, correo FROM Notificacion INNER JOIN Servicios 
                    ON Servicios.idServicio = Notificacion.idServicio 
                    INNER JOIN Usuario ON idReceptor = Usuario.idUsuario
                    WHERE (idEmisor = \"{username}\" AND tipo = \"ACCEPTED\") AND Notificacion.estado = 1
                """

    queryResult3 = dbHandler.SQL_execute_twoway_statement(query3)

    for service in queryResult3:
        
        data["notificaciones"].append({
                    "idNot": service[0],
                    "idEmisor": service[1],
                    "idReceptor": service[2],
                    "idServicio": service[3],
                    "tipo": "CONTACTING",
                    "nombre": service[5],
                    "descripcion": service[6],
                    "nombreUsuario": service[7],
                    "nombreApellidoP": service[8],
                    "nombreApellidoM": service[9],
                    "correo": service[10]
                    })

    query4 = f"""SELECT idNotificacion, idEmisor, idReceptor, Notificacion.idServicio, tipo, Servicios.nombre, descripcion, Usuario.nombre, apellidoP, apellidoM, correo FROM Notificacion INNER JOIN Servicios 
                    ON Servicios.idServicio = Notificacion.idServicio
                    INNER JOIN Usuario ON Servicios.idUsuario = Usuario.idUsuario
                    WHERE (idReceptor = \"{username}\" AND tipo = \"ACCEPTED\" ) AND Notificacion.estado = 1
                """

    queryResult4 = dbHandler.SQL_execute_twoway_statement(query4)

    for service in queryResult4:
        
        data["notificaciones"].append({
                    "idNot": service[0],
                    "idEmisor": service[1],
                    "idReceptor": service[2],
                    "idServicio": service[3],
                    "tipo": service[4],
                    "nombre": service[5],
                    "descripcion": service[6],
                    "nombreUsuario": service[7],
                    "nombreApellidoP": service[8],
                    "nombreApellidoM": service[9],
                    "correo": service[10]
                    })

                    
    dbHandler.SQL_stop()

    return data

def lambda_handler(event, context):

    username = event["username"]

    


    data = getNotifications(username)
    

    return data