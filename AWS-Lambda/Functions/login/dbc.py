import mysql.connector as mysql

class DBC:
    def __init__(self):
        self.mySQLConfig = {
                        'user': 'BancoDeTiempo',
                        'password': 'BancoDeTiempo123',
                        'host': 'bancodetiempo.cx0t9juk5mxq.us-east-1.rds.amazonaws.com',
                        'database': 'BancoDeTiempo',
                        'raise_on_warnings': True
                        }
        


    def SQL_initialize(self):
        self.connection = mysql.connect(**self.mySQLConfig)

    def SQL_stop(self):
        self.connection.close()
        
    def SQL_execute_oneway_statement(self,query):
        try:
            statement = self.connection.cursor()

            statement.execute(query)

            self.connection.commit()

            statement.close()

            queryExecuted = True
        except TypeError as e:
            queryExecuted = False

        
        return queryExecuted
    
    def SQL_execute_twoway_statement(self,query):
        try:
            statement = self.connection.cursor()

            statement.execute(query)

            data = []

            queryResult = statement.fetchone()

            while (queryResult != None):
                registry = queryResult
                data.append(registry)

                queryResult = statement.fetchone()
            
            # print(data)
            
            statement.close()
        except Exception as e:
            
            data = "Error in query"
        return data
