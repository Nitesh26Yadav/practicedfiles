import json
import pymssql
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

cust = "/customersdata"

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
        response = getcustomersdata(requestbody['queryStringParameters']['RuleId'])
    
    # elif httpMethod == 'DELETE' and path == cust:
    #     requestbody = event
    #     # response = deletecustomersdata(requestbody['queryStringParameters']['RuleInfo'])
        
    elif httpMethod == 'PATCH' and path == cust:
        requestBody = json.loads(event['body'])
        response = modifycustomersdata(requestBody['first_id']['RuleId'],requestBody['first_id']['RuleGuid'],requestBody['first_id']['RuleTypeId'],requestBody['first_id']['SubTypeID'],requestBody['first_id']['RuleDescription'],requestBody['first_id']['StartDate'],requestBody['first_id']['EndDate'],requestBody['first_id']['RunFrequency'],requestBody['first_id']['LastRunDate'],requestBody['first_id']['NextRunDate'],requestBody['first_id']['ApprovalRequired'],requestBody['first_id']['PushNotificationMessage'],requestBody['first_id']['NotificationTime'],requestBody['first_id']['UpdateGroupStats'],requestBody['first_id']['NotifyAdminPostRun'],requestBody['first_id']['RuleNotificationEmail'],requestBody['first_id']['CreateGroupOnlyNoOfferRequired'],requestBody['first_id']['CreatedBy'],requestBody['first_id']['CreateDateTime'],requestBody['first_id']['UpdatedBy'],requestBody['first_id']['UpdateDateTime'],requestBody['first_id']['RuleStatus'],requestBody['first_id']['RSAClientID'],requestBody['first_id']['RSAClientGuid'],requestBody['second_id']['ApcriteriaId'],requestBody['second_id']['APRuleId'],requestBody['second_id']['InLastDays'],requestBody['second_id']['NTimesPurchased'],requestBody['second_id']['TopNCustomers'],requestBody['second_id']['AmountPurchased'],requestBody['second_id']['PurchasedUPCs'],requestBody['second_id']['PurchasedDepts'],requestBody['second_id']['StoreList'],requestBody['second_id']['ZipCodeList'],requestBody['second_id']['CustomerSince'],requestBody['second_id']['CreateDateTime'],requestBody['second_id']['UpdateDateTime'],requestBody['second_id']['IsTierBased'],requestBody['second_id']['TierTypeID'],requestBody['second_id']['CriteriaStatus'],requestBody['second_id']['TierName'])

    else:
        response = buildResponse(404,'Not Found') 
        
    return {
            'body': json.dumps(response,default=str)
        }


def getcustomersdata(Rule):
    try:
        table.execute(f"SELECT * from AP_Rules WHERE RuleId = {Rule}")
        headers = [x[0] for x in table.description]
        result = table.fetchall()
        
        data = []
        for res in result:
            var1 = (dict(zip(headers,res)))
            data.append(var1)
        conn.commit()
        
        
        table.execute(f"SELECT * from AP_Rules_Criteria WHERE ApRuleId = {Rule}")
        headers = [x[0] for x in table.description]
        result = table.fetchall()
        
        data1 = []
        for res in result:
            var1 = (dict(zip(headers,res)))
            data1.append(var1) 
        conn.commit()
        data2 = [data,data1]
        
        return buildResponse(200,data2)
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
        table.execute(f"exec ap_update_rule @Rule_guid = '{body['first_id']['RuleInfo']}',@Rule_Type_Id = '{body['first_id']['Rule_Type_Id']}',@Rule_Description = '{body['first_id']['Rule_Description']}',@Rule_Sub_Type_Id = '{body['first_id']['Rule_Sub_Type_Id']}',@No_Offer = '{body['first_id']['No_Offer']}',@Run_Frequency = '{body['first_id']['Run_Frequency']}',@Start_Date = '{body['first_id']['Start_Date']}',@End_Date = '{body['first_id']['End_Date']}',@Rule_Notification_Email = '{body['first_id']['Rule_Notification_Email']}',@Approval_Required = '{body['first_id']['Approval_Required']}',@Push_Message = '{body['first_id']['Push_Message']}',@Push_Time = '{body['first_id']['Push_Time']}',@Notify_Admin_Post_Run = '{body['first_id']['Notify_Admin_Post_Run']}',@Update_Group_Stats = '{body['first_id']['Update_Group_Stats']}',@RSAClientID = '{body['first_id']['RSAClientID']}',@RSAClientGuid = '{body['first_id']['RSAClientGuid']}',@Rule_Status = '{body['first_id']['Rule_Status']}',@Created_By = '{body['first_id']['Created_By']}'")
        
        headers = [x[0] for x in table.description]
        result = table.fetchall()
        conn.commit()

        for res in result:
            aprul = (dict(zip(headers,res)))
            id1 = aprul['RuleId']
            guid = aprul['RuleGuid']

        table.execute(f"exec ap_update_rule_criteria @Rule_Criteria_Id= '{body['second_id']['Rule_Criteria_Id']}',@Rule_Id = {id1},@In_Last_Days = {body['second_id']['In_Last_Days']},@Times_Purchased ={body['second_id']['Times_Purchased']},@Amount_Spend ='{body['second_id']['Amount_Spend']}',@TopNCustomers = '{body['second_id']['TopNCustomers']}',@ZipCodeList = {body['second_id']['ZipCodeList']},@Is_Tier_Based= {body['second_id']['Is_Tier_Based']},@Tier_Name = {body['second_id']['Tier_Name']},@Rule_Criteria_Status = {body['second_id']['Rule_Criteria_Status']},@Created_By = '{body['second_id']['Created_By']}'") 
        headers = [x[0] for x in table.description]
        result1 = table.fetchall()
        conn.commit()

        for res1 in result1:
            apcri = (dict(zip(headers,res1)))
        data = (aprul,apcri)
        
        requestbody = {
            'Operation': 'SAVE',
            'Message'  :'SUCCESS',
            'Item' : data
        } 
            
        return buildResponse(200,requestbody)
    except:
        logger.exception('Do your custom error handling here')
        table.execute(f"exec ap_delete_rule @Rule_guid = '{guid}',@Created_by = '{body['first_id']['Created_By']}'") 
        conn.commit()
        
        return buildResponse(404,'Initial rule Inserted and also deleted!')
            
            
def modifycustomersdata(ruleid,ruleguid,ruletypeid,subtypeid,ruledescription,startdate,enddate,runfrequency,lastrundate,nextrundate,approvalrequired,pushnotificationmessage,notificationtime,updategroupstats,notifyadminpostrun,rulenotification,creategroupnooffer,createdby,createdatetime,updatedby,updatedatetime,rulestatus,rsaclientid,rsaclientguid,apcriteriaid,apruleid,inlastdays,ntimespurchased,topncustomers,amountpurchased,purchasedupcs,purchasedepts,storelist,zipcodelist,customersince,createdatime,updatedtime,istierbased,tiertypeid,criteriastatus,tiername):
    try:
        table.execute(f"exec ap_update_rule @Rule_Guid = '{ruleguid}',@Rule_Type_Id = '{ruletypeid}',@Rule_Description = '{ruledescription}',@Rule_Sub_Type_Id = '{subtypeid}',@No_Offer = '{creategroupnooffer}',@Run_Frequency = '{runfrequency}',@Start_Date = '{startdate}',@End_Date = '{enddate}',@Rule_Notification_Email = '{rulenotification}',@Approval_Required = '{approvalrequired}',@Push_Message = '{pushnotificationmessage}',@Push_Time = '{notificationtime}',@Notify_Admin_Post_Run = '{notifyadminpostrun}',@Update_Group_Stats = '{updategroupstats}',@RSAClientID = '{rsaclientid}',@RSAClientGuid = '{rsaclientguid}',@Rule_Status = '{rulestatus}',@Created_By = '{createdby}'")
        conn.commit()
        table.execute(f"exec ap_update_rule_criteria @Rule_Criteria_Id= '{apcriteriaid}',@Rule_Id = {apruleid},@In_Last_Days = {inlastdays},@Times_Purchased ={ntimespurchased},@Amount_Spend ='{amountpurchased}',@TopNCustomers = '{topncustomers}',@ZipCodeList = {zipcodelist},@Is_Tier_Based= {istierbased},@Tier_Name = {tiername},@Rule_Criteria_Status = {criteriastatus},@Created_By = '{createdby}'") 
        conn.commit()

        body = {
            'operation':'PATCH',
            'Message':'SUCCESS'
        }
        return buildResponse(200,body)

    except:
        logger.exception("Do your Custom error handling here.")
        
        table.execute(f"exec ap_delete_rule @Rule_guid = '{ruleguid}',@Created_by = '{createdby}'") 
        conn.commit()
        return buildResponse(404,'Insert has been Failed!')
    
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
