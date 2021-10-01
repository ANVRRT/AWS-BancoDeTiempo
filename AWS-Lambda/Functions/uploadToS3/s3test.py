import json
import boto3

def upload_to_s3():
    try:
        s3 = boto3.client('s3')
        
        bucket = "bancodetiempotest"
        
        transaction = {}
        transaction["name"] = "Test"
        transaction["type"] = "Testing"
        transaction["amount"] = 20
        
        filename = "Test" + ".json"
        
        byteFile = bytes(json.dumps(transaction).encode('UTF-8'))
        
        s3.put_object(Bucket = bucket, Key = filename, Body = byteFile)
        
        return 1
    except:
        return 0

def get_to_s3():

    s3 = boto3.client('s3')
    
    bucket = "bancodetiempotest"
    
    
    filename = "FotoZoom" + ".jpg"
    
    
    obj = s3.get_object(Bucket = bucket, Key = filename)
    
    obj = obj['Body'].read()
    
    
    return obj

def lambda_handler(event, context):
    # TODO implement
    #test = upload_to_s3()
    test2 = get_to_s3()
    return test2
