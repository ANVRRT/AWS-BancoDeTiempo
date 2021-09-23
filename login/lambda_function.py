import json

def hello_world(name):
    test = f'Hello World {name}'
    return test

def lambda_handler(event, context):
    test = hello_world(event['name'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'response': test
    }
