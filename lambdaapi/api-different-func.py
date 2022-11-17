import json


def lambda_handler(event,context):
    # print(event)
    if event['httpMethod'] == 'GET':
        result = get_logic(event)
    
    elif event['httpMethod'] == 'POST':
        result = post_logic(json.loads(event['body']))
        

    return {
        'body':json.dumps(result)
        }

def get_logic(event):
    requiredStrings = ['domainName','body','resource','stage']
    keys = list(event.keys()) 
    # data = json.loads(event['body'])
    
    mainRequiredStrings = []
    remainingRequiredStrings = requiredStrings
    getResult =[]
    
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
                        getResult.append(result)
                        
        
        for eachString in mainRequiredStrings:
                if eachKey == eachString:
                    result = event[eachKey]
                    getResult.append(result)
                    
    return (getResult)
    
def post_logic(percent):
    postresult = []
    for eachStudent in percent:
        marksData = eachStudent['marks']
        name = eachStudent['Name']
        marks = marksData.values()
        length =len(marks)
        filResult = sum(marks)
        totalmarks = length*100
        percentage = (filResult/totalmarks)*100
        
        
        per = (f"{name} got {int(percentage)}% on his Academics")
        postresult.append(per)

    return (postresult)
