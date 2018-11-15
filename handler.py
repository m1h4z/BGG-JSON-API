import json


def pong(event, context):
    body = {
        "message": "Pong"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response