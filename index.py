import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World. Its me',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    print("Hello")
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
