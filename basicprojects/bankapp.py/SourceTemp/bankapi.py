import json
from CommonApis import ValidateRequest, connectdb, AccessDBData
import logging
import string
import random

log = logging.getLogger()
log.setLevel(logging.INFO)


def Response(HttpCode, Msg):
    log.info(f"-- Api Response --{Msg}")

    return {
        "StatusCode": HttpCode,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
        },
        "body": json.dumps({Msg})
    }


def Createuser(event):

    body = json.loads(event['body'])

    data = ValidateRequest(body, "register")
    if not data[0]:
        return Response(400, f"Bad Request - {data[1]}")
    body = data[1]

    AccountNo = ''.join(random.choice(string.digits)
                        for _ in range(16))
    try:
        Query = f"exec {AccountNo}, '{body['first_name']}', '{body['last_name']}', '{body['email']}', '{body['mobile_number']}', '{body['address']}', '{body['password']}'"
    except KeyError as e:
        log.error(f" Missing parameter-{e}")
        return Response(400, f"Bad Request -{e}")

    conn = connectdb()
    UserData = AccessDBData("exec update_register_data", Query)
    if not UserData:
        return Response(400, "Failed to Create User")
    else:
        return Response(200, UserData)
