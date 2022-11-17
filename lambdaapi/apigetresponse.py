import json 

def lambda_handler(event,context):
    print(event)
    requiredStrings = ['httpMethod','body','resource','stage']
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
                    
                    
    
    #TODO implement
    return {
        'statusCode':200,
        'body':json.dumps(finalResult)
    }
    

