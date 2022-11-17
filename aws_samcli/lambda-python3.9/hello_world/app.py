import json

# import requests


def lambda_handler(event, context):
    name = event['first_name']
    wishes = event['wishes']
    
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": (f"hello {name} {wishes}"),

            }
        ),
    }
