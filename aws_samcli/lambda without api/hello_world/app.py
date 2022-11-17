import json

def lambda_handler(event,context):

    name = event['name']
    information = event['information']

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": (f"hello {name} {information}"),
                # "location": ip.text.replace("\n", "")
            }
        ),
    }
    