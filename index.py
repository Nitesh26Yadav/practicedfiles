import json

def lambda_handler(event,context):
    value = 10
    quantity = 5

    total = value * quantity

    return {
    "statusCode": 200,
    "body": json.dumps(
        {
            "message": (f"hello your function has been updated. The total value is{total}"),
            

        }
    ),
}
