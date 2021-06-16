import json


def hello(event, context):
    body = {
        "message": "Hello ChowNow! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}


def echo(event, context):
    """Echos back event body passed to the function."""
    print(f'Passed event has type:{type(event)}')

    return {"statusCode": 200, "body": json.dumps(event)}
