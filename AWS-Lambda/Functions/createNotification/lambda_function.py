from dbc import DBC


def define_query(data):

    if data["tipo"] == "REQUEST":
        query = f"""INSERT INTO Notificacion VALUES(
                    NULL,
                    \"{data["idEmisor"]}\",
                    \"{data["idReceptor"]}\",
                    \"{data["idServicio"]}\",
                    \"{data["tipo"]}\"
                    )
                    """
    else:
        query = f"UPDATE Notificacion SET tipo = \"{data['tipo']}\" WHERE idNotificacion = {data['idNot']}"

    return query



def process_notification(dataReceived):

    dbHandler = DBC()
    dbHandler.SQL_initialize()

    query = define_query(dataReceived)

    transactionApproval = 1

    queryResult = dbHandler.SQL_execute_oneway_statement(query)

    if not queryResult:
        transactionApproval = 0

    data = {
            "transactionApproval": transactionApproval
            }

    return data

def lambda_handler(event, context):

    if event["type"] == "REQUEST":

        data = {
                "idServicio": event["idServicio"],
                "idEmisor": event["idEmisor"],
                "idReceptor": event["idReceptor"],
                "tipo": event["type"]
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