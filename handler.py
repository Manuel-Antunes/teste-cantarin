import json


def hello(event, context):
    body = json.loads(event['body'])
    
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
