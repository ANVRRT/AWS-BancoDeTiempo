import json
from dbc import DBC

def approve_all(username):
    pass

def approve_ine(username):
    pass

def approve_comprobante(username):
    pass

def approve_carta(username):
    pass

import json
from dbc import DBC

def lambda_handler(event, context):
    
    id1 = event['queryStringParameters']['username']
    id2 = event['queryStringParameters']['type']

    transaction = {}
    
    transaction["id"] = id1
    transaction["type"] =id2

    responseObject = {}
    
    responseObject['statusCode'] = 200
    responseObject['body'] = json.dumps(transaction)
    
    return responseObject
