import json


def lambda_handler(event,context):
    print(event)


    def get_logic():
        requiredStrings = ['domainName','resource','stage']
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
                        
        return(getResult)
                        
    def post_logic():
        postresult = []
        percent =json.loads(event['body'])
        for eachStudent in percent:
            marksData = eachStudent['marks']
            name = eachStudent['Name']
            marks = marksData.values()
            length =len(marks)
            filResult = sum(marks)
            totalmarks = length*100
            percentage = (filResult/totalmarks)*100
            
            
            per = (f"{name} got {percentage}% on his Academics")
            postresult.append(per)

        return(postresult)
            
    
    update_result = post_logic()
    fetch_result = get_logic()


    if event['httpMethod'] == 'GET':
        return{'body':json.dumps(fetch_result)}
        
    elif event['httpMethod'] == 'POST':
        return{'body':json.dumps(update_result)}
