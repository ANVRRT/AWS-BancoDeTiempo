import mysql.connector      

class DBC:

    def __init__(self):
        self.mySQLConfig = {
                'user': 'sql5436993',
                'password': 'v7F7jRWVFc',
                'host': 'sql5.freesqldatabase.com',
                'database': 'sql5436993',
                'raise_on_warnings': True
                }
    def SQL_initialize(self):
        self.connection = mysql.connector.connect(**self.mySQLConfig)