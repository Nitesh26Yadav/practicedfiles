import json
import pymssql
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

cust = "/customersdata"
cust1 = "/totalcustomers"


conn = pymssql.connect(
            server='database-1.cxrjyosgnij0.ap-south-1.rds.amazonaws.com', 
            user='admin', 
            password='Veritra2022', 
            database='employeedata')

table = conn.cursor()


def lambda_handler(event,context):
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']
    
    if httpMethod == 'POST' and path == cust:
        response = savecustomersdata(json.loads(event['body']))
    
    elif httpMethod == 'GET' and path == cust:
        requestbody = event
        response = getcustomersdata(requestbody['queryStringParameters']['RuleInfo'])
    
    elif httpMethod == 'GET' and path == cust1:
        response = totalcustomersdata()
        
    elif httpMethod == 'DELETE' and path == cust:
        requestbody = event
        response = deletecustomersdata(requestbody['queryStringParameters']['RuleInfo'])
    else:
        response = buildResponse(404,'Not Found') 
        
    return {
            'body': json.dumps(response,default=str)
        }


def getcustomersdata(Rule):
    try:
        table.execute(f"SELECT * from AP_Rules WHERE RuleInfo = '{Rule}'")
        headers = [x[0] for x in table.description]
        result = table.fetchall()
        
        data = []
        for res in result:
            var1 = (dict(zip(headers,res)))
            data.append(var1)
        conn.commit()
        return buildResponse(200,data)
    except:
        logger.exception('Do your custom error handling here.')
        
def totalcustomersdata():
    try:
        table.execute(f"SELECT * from AP_Rules where RuleStatus = {1}")
        headers = [x[0] for x in table.description]
        result = table.fetchall()
        
        data = []
        for res in result:
            var1 = (dict(zip(headers,res)))
            data.append(var1)
        conn.commit()
        return buildResponse(200,data)
    
    except:
        logger.exception("do your custom handling here.")
        
def savecustomersdata(body):
    try:
        table.execute(f"exec ap_update_rule @RuleInfo ='{body['RuleInfo']}',@Rule_Guid = '{body['Rule_Guid']}',@Rule_Type_Id = '{body['Rule_Type_Id']}',@Rule_Description = '{body['Rule_Description']}',@Rule_Sub_Type_Id = '{body['Rule_Sub_Type_Id']}',@No_Offer = '{body['No_Offer']}',@Run_Frequency = '{body['Run_Frequency']}',@Start_Date = '{body['Start_Date']}',@End_Date = '{body['End_Date']}',@Rule_Notification_Email = '{body['Rule_Notification_Email']}',@Approval_Required = '{body['Approval_Required']}',@Push_Message = '{body['Push_Message']}',@Push_Time = '{body['Push_Time']}',@Notify_Admin_Post_Run = '{body['Notify_Admin_Post_Run']}',@Update_Group_Stats = '{body['Update_Group_Stats']}',@RSAClientID = '{body['RSAClientID']}',@RSAClientGuid = '{body['RSAClientGuid']}',@Rule_Status = '{body['Rule_Status']}',@Created_By = '{body['Created_By']}'")
        
        conn.commit()
        
        requestbody = {
            'Operation': 'SAVE',
            'Message'  :'SUCCESS',
            'Item': body
        } 
        return buildResponse(200,requestbody)
    except:
        logger.exception('Do your custom error handling here')
            

def deletecustomersdata(rule):
    
    try:
        table.execute(f"UPDATE AP_Rules set RuleStatus = {2} where RuleInfo = '{rule}'")
        table.execute (f"SELECT * from AP_Rules where RuleInfo = '{rule}'and RuleStatus = {2}")
        headers = [x[0] for x in table.description]
        result = table.fetchall()
        
        data = []
        for res in result:
            var1 = (dict(zip(headers,res)))
            data.append(var1)
        conn.commit()

        requestbody = {
            'operation':'DELETE',
            'Message':'SUCCESS',
            'Item' : data
        }
        return buildResponse(200,requestbody)
        
    except:
        logger.exception("Do your custom handling here.")
        
        
        
def buildResponse(statusCode,body=None):
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
