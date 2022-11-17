import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodbTableName = 'employees_data'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)

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
        requestBody = event
        response = getemployeedata(requestBody['queryStringParameters']['emp_id'])

    elif httpMethod == getmethod and path == idsPath:
        response = getemployeeids()

    elif httpMethod == postmethod and path == empidsPath:
        response = saveemployeedata(json.loads(event['body']))

    elif httpMethod == patchmethod and path == empidsPath:
        requestBody = json.loads(event['body'])
        response = modifyemployeedata(requestBody['emp_id'],requestBody['Name'],requestBody['Job'])
    
    elif httpMethod == deletemethod and path == empidsPath:
        requestBody = event
        response = deleteemployeedata(requestBody['queryStringParameters']['emp_id'])

    else:
        response = buildResponse(404,'Not Found')

    return {
        'body':json.dumps(response)
        }


def getemployeedata(emp_id):
    
    try:
        response = table.get_item(
            Key = {
                'emp_id':emp_id
            }
        )
        if 'Item' in response:
            return buildResponse(200,response['Item'])
        else:
            return buildResponse(404,{'message': 'Employeeid : {} is not found'.format(emp_id)})

    except:
        logger.exception('Do your custom error handling here.')

def getemployeeids():
    
    try:
        response = table.scan()
        result = response['Items']
            
        while 'LastEvaluateKey' in response:
            response = table.scan(ExclusiveStartKey = response['LastEvaluateKey'])
            result.extend(response['Items'])
            
        body = {
            'employeeids' :result
        }
        return buildResponse(200,body)
        
    except:
        logger.exception('Do your custom error handling here.')


def saveemployeedata(requestBody):
    msg = 0
    try:
        requestStrings = requestBody.keys()
        requiredStrings = ['emp_id','Name','Job']
        
        for each in requestStrings:
            for each1 in requiredStrings:
                if (each== each1):
                    msg = msg+1
        
        if (msg == 3):
            response = table.put_item(Item = requestBody)
            body = {
                'Operation': 'SAVE',
                'Message'  :'SUCCESS',
                'Item':response
                
            }
            return buildResponse(200,body)
        else:
            return {"message" :"Please Enter valid Keys for the request Body"}
    except:
        logger.exception('Do your custom error handling here.')        


def modifyemployeedata(emp_id,Name,Job):
    try:
        response = table.update_item(
            Key = {'emp_id':emp_id},
            
            UpdateExpression = 'set #N =:n, #J = :j',
            ExpressionAttributeNames={
                '#N': 'Name',
                '#J': 'Job'
            },
            ExpressionAttributeValues = {
                ':n': Name,
                ':j': Job
            },
                ReturnValues = 'UPDATED_NEW',
            )
        body = {
            'Operation': 'SAVE',
            'Message'  :'SUCCESS',
            'UpdateAttributes': response
        }
        return buildResponse(200,body)
    except:
        logger.exception('Do your custom error handling here.')  

def deleteemployeedata(emp_id):
    try:
        response = table.delete_item(
            Key = {
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
            'Access-Control-Allow-Origin':'*',
            
        }
    }
    if body is not None:
        response['body'] = (body)
    return response
