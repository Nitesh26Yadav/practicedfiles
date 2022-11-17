import json 

event = {'resource': '/empdata', 'path': '/empdata', 'httpMethod': 'POST', 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Cache-Control': 'no-cache', 'Content-Type': 'application/json', 'Host': '54t19y1qo5.execute-api.ap-south-1.amazonaws.com', 'Postman-Token': '08c54fba-031d-48df-bed1-d2b2c9827e0d', 'User-Agent': 'PostmanRuntime/7.29.2', 'X-Amzn-Trace-Id': 'Root=1-6304ff88-54d2ec4a7612338e5299b675', 'X-Forwarded-For': '27.6.123.188', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['*/*'], 'Accept-Encoding': ['gzip, deflate, br'], 'Cache-Control': ['no-cache'], 'Content-Type': ['application/json'], 'Host': ['54t19y1qo5.execute-api.ap-south-1.amazonaws.com'], 'Postman-Token': ['08c54fba-031d-48df-bed1-d2b2c9827e0d'], 'User-Agent': ['PostmanRuntime/7.29.2'], 'X-Amzn-Trace-Id': ['Root=1-6304ff88-54d2ec4a7612338e5299b675'], 'X-Forwarded-For': ['27.6.123.188'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'e27867', 'resourcePath': '/empdata', 'httpMethod': 'POST', 'extendedRequestId': 'XUzdVGRLBcwFnpg=', 'requestTime': '23/Aug/2022:16:25:44 +0000', 'path': '/cam/empdata', 'accountId': '206239526750', 'protocol': 'HTTP/1.1', 'stage': 'cam', 'domainPrefix': '54t19y1qo5', 'requestTimeEpoch': 1661271944313, 'requestId': '2c83db76-4c7a-4e5b-bdf0-c514f305bae3', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '27.6.123.188', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'PostmanRuntime/7.29.2', 'user': None}, 'domainName': '54t19y1qo5.execute-api.ap-south-1.amazonaws.com', 'apiId': '54t19y1qo5'}, 'body': '[\r\n\t{\r\n\t\t"Studentid": 1,\r\n\t\t"Name": "Nitesh",\r\n\t\t"marks": {"Maths":75,"Social":88,"Science":35}\r\n\t},\r\n\t{\r\n\t\t"Studentid": 2,\r\n\t\t"Name": "Angel",\r\n\t\t"marks": {"Maths":68,"Social":98,"Science":85}\r\n\t}\r\n\t\r\n]', 'isBase64Encoded': False}


def lambda_handler(event):
    
    # print(event)
    requiredStrings = ['domainName','body','resource','stage']
    keys = list(event.keys()) 
    
    
    mainRequiredStrings = []
    remainingRequiredStrings = requiredStrings
    finalResult =[]
    
    
    for eachKey in keys:
        for  eachString in requiredStrings:
            if eachString == eachKey:
                mainRequiredStrings.append(eachKey)
                remainingRequiredStrings.remove(eachKey)
    
    for eachKey in keys:
        element=event[eachKey]
        elementtype = type(element)
        if elementtype == dict:
            childkey = list(element.keys())
            for eachchildkey in childkey:
                for eachString in remainingRequiredStrings:
                    if eachString == eachchildkey:
                        result = element[eachString]
                        finalResult.append(result)
                        
        
        for eachString in mainRequiredStrings:
                 if eachKey == eachString:
                    result = event[eachKey]
                    finalResult.append(result)


    firstResult = json.dumps(finalResult)
                    
    percent1 = []
    percent = json.loads(event['body'])
    for each in percent:
        marksdata = each['marks']
        name = each['Name']
        marks = marksdata.values()
        length = len('marks')
        filResut = sum(marks)
        totalmarks = length*100
        percentage = filResut/totalmarks*100
        
        per = (f"{name} got {percentage}% on his Academics")
        percent1.append(per)
   
    finalResult2 =json.dumps(percent1)


    if event['httpMethod'] == 'POST':
        print(finalResult2)
        
    elif event['httpMethod'] == 'GET':
        print(firstResult)
        
lambda_handler(event)
