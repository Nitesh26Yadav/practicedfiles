import jwt
import pymssql
import logging
from jsonschema import validate, ValidationError
import pymssql

log = logging.getLogger()
log.setLevel(logging.INFO)


def ValidateRequest(data, schema):
    if schema == "register":
        schema = {
            "type": "object",
            "properties": {
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "email": {"type": "string"},
                "mobile_number": {"type": "number", "maxlength": 10},
                "address": {"type": "string"},
                "password": {"type": "string"}
            },
            "required": ["first_name", "last_name", "email", "mobile_number", "address", "password"]
        }

    optionals = [key for key in schema["properties"].keys()
                 if key not in schema["required"]]
    for i in optionals:
        if i not in data:
            data[i] = None

    try:
        validate(instance=data, schema=schema)
        log.info(f"--Validated JSON Schema of {schema}")
    except ValidationError as e:
        log.error(f" Error in Schema Please check {schema} --{e}")
        return [False, e]
    else:
        return [True, data]


def connectdb():
    server = 'database-1.cxrjyosgnij0.ap-south-1.rds.amazonaws.com',
    user = 'admin',
    password = 'Veritra2022',
    database = 'employeedata'

    try:
        conn = pymssql.connect(server=server, user=user,
                               password=password, database=database)
        print('DB Connected')
        return conn
    except pymssql.Error as e:
        log.error(f"-DB Connection Error - {e}")
        print(f'DB Connection Error - {e}')
        return Response(500, "Something went wrong, Please try again")
