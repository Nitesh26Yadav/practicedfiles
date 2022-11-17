import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)



s3_client= boto3.client('s3',
        aws_access_key_id= "AKIATABGVN5PEF4BS5PR",
        aws_secret_access_key="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")


dynamodbTablName = 'employees_data'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTablName)

getmethod = "GET"
postmethod ="POST"
patchmethod = "PATCH"
deletemethod = "DELETE"
idsPath = "/employeeids"
empidsPath = "/employeeid"


def lambda_handler(event,context):
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']

    if httpMethod == getmethod and path == empidsPath:
        response = getemployeedata(event['queryStringParameters']['emp_id'])

    elif httpMethod == getmethod and path == idsPath:
        pass

    elif httpMethod == postmethod and path == empidsPath:
        requestBody = json.loads(event['body'])
        response = saveemployeedata(requestBody['body'])

    elif httpMethod == patchmethod and path == empidsPath:
        requestBody = json.loads(event['body'])
        response = modifyemployeedata(requestBody['emp_id'],requestBody['updateKey'],requestBody['updateValue'])
    
    elif httpMethod == deletemethod and path == empidsPath:
        requestBody = json.loads(event['body'])
        response = deleteemployeedata(requestBody['emp_id'])

    else:
        response = buildResponse(404,'Not Found')

    return response

#res = lambda_handler(event,context)

def getemployeedata(emp_id):
    
    try:
        response = table.get_item(
            key = {
                'emp_id':emp_id
            }
        )
        if 'Item' in response:
            return buildResponse(200,response['Item'])
        else:
            return buildResponse(404,{'message': 'Employeeid : {} is not found'.format(emp_id)})

    except:
        logger.exception('Do your custom error handling here.')

def saveemployeedata(table,requestBody):
    try:
        response = table.put_item(Item=requestBody)
        body = {
            'Operation': 'SAVE',
            'Message'  :'SUCCESS',
            'Item': response
        }
        return buildResponse(200,body)
    except:
        logger.exception('Do your custom error handling here.')        


def modifyemployeedata(table,emp_id,updateKey,updateValue):
    try:
        response = table.update_item(
            key = {
                'emp_id':emp_id
            },
            UpdateExpression = 'set %s  = value' %updateKey,
            ExpressionAttributeValues = {
                'value': updateValue
            },
            ReturnValues = 'UPDATED_NEW'
        )
        body = {
            'Operation': 'SAVE',
            'Message'  :'SUCCESS',
            'UpdateAttributes': response
        }
        return buildResponse(200,body)
    except:
        logger.exception('Do your custom error handling here.')  

def deleteemployeedata(table,emp_id):
    try:
        response = table.delete_item(
            key = {
                'emp_id':emp_id
            },
            ReturnValues = 'ALL_OLD'
        )
        body = {
            'operation':'DELETE',
            'Message':'SUCCESS',
            'DeletedItem': response
        }
        return buildResponse(200,body)
    except:
        logger.exception('Do your custom error handling here.')  


def buildResponse(statusCode,body = None):
    response = {
        'statusCode':statusCode,
        'headers':{
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin':'*'
        }
    }
    if body is not None:
        response['body'] = json.dumps(body)





