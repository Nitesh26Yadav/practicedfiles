# import requests
# import os


# # conn = "https://0ry7jslpr3.execute-api.us-east-1.amazonaws.com/dev/rule"
# conn = os.environ.get("API")
# guid = 'F36DF97E-F80C-44C1-A64F-6BE5D07FD298'
# UID = 1
# # query = f"exec ap_get_rule {guid}, {UID}"


# # filterdata = []
# # for x in query.split():
# # 	if x == 'exec':
# # 		pass
# # 	elif x != 'exec':
# # 		filterdata.append(x)
# # proc_name = filterdata[0]
# # data = filterdata[1:]

# # args_name = str(data).replace('[','').replace(']','')
# # print(args_name)


# # query = "exec ap_get_rule_stores 1"
# # query = f"exec ap_get_rule 'F36DF97E-F80C-44C1-A64F-6BE5D07FD298',1"
# # print(query)
# # query = "exec ap_get_rule F36DF97E-F80C-44C1-A64F-6BE5D07FD298 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VySUQiOjEwMSwiaXNfY29uc2VudF9wcm92aWRlZCI6dHJ1ZSwidXNlcm5hbWUiOiJkZW1vdXNlckBhdXRvcGlsb3QuY29tIiwidXNlcl9ndWlkIjoiN0UyOTExMDUtRDQyNy00QTRDLThGOEMtMUE5MUFCOUY3QTMzIiwiZmlyc3RfbmFtZSI6IkpvaG4iLCJsYXN0X25hbWUiOiJGYXJtcyIsInJldGFpbGVyIjp7ImlkIjo0OCwic2NvcGVzIjpbXX0sImV4cGlyZXNfaW4iOiIyMDIyLTAzLTA1IDE4OjQ3OjIzLjQyMjI2MCJ9.EhC9HR6vgi0dqmD24TpDpe4FEee1VT4p311zHACDk8k"
# # query =  f"exec ap_get_rule '{guid}',{UID}"

# # query = "exec ap_update_rule_departments"

# # query = "exec ap_update_rule_offer 0 "
# # # query = "exec ap_update_rule ''
# query = "exec ap_get_rule_top_n_shoppers 0"

# # print(type("'F36DF97E-F80C-44C1-A64F-6BE5D07FD298',1"))

# def Accessdbdata(conn,query):

# 	try:
# 		filterdata = []
# 		for x in query.split():
# 			if x == 'exec':
# 				pass
# 			elif x != 'exec':
# 				filterdata.append(x)
# 		proc_name = filterdata[0]
# 		# print(proc_name)
# 		data = filterdata[1:]
# 		# print(data)

# 		name = ""
# 		args_name = name.join(data)
# 		# print(args_name)
# 		body = {

# 		"Instance":"veritra",

# 		"DB":"RSA_CentMark",

# 		"Proc": proc_name,

# 		"Args": args_name

# 		}
# 		response = requests.post(conn,json = body)
# 		# print(proc_name)
# 		# print(args_name)

# 		rules = response.json()
# 		return rules['Message']

# 	except:
# 		return False

# data = Accessdbdata(conn,query)
# print(data)


# 		# "Instance":"veritra",

# 		# "DB":"RSA_CentMark",

# 		# "Proc":"ap_get_rule",

# 		# "Args":"F36DF97E-F80C-44C1-A64F-6BE5D07FD298, eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VySUQiOjEwMSwiaXNfY29uc2VudF9wcm92aWRlZCI6dHJ1ZSwidXNlcm5hbWUiOiJkZW1vdXNlckBhdXRvcGlsb3QuY29tIiwidXNlcl9ndWlkIjoiN0UyOTExMDUtRDQyNy00QTRDLThGOEMtMUE5MUFCOUY3QTMzIiwiZmlyc3RfbmFtZSI6IkpvaG4iLCJsYXN0X25hbWUiOiJGYXJtcyIsInJldGFpbGVyIjp7ImlkIjo0OCwic2NvcGVzIjpbXX0sImV4cGlyZXNfaW4iOiIyMDIyLTAzLTA1IDE4OjQ3OjIzLjQyMjI2MCJ9.EhC9HR6vgi0dqmD24TpDpe4FEee1VT4p311zHACDk8k".split(',')


# # response = requests.post(conn,json={

# #     "Instance":"veritra",

# #     "DB":"RSA_CentMark",

# #     "Proc":"ap_get_rule_top_n_shoppers",

# #     "Args":"0"

# # })


# # filterdata = ""

# # for x in query.split():
# # 	if x == 'exec':
# # 		pass
# # 	elif x != 'exec':
# # 		filterdata = filterdata +" "+ str(x)

# # data = filterdata.replace(' ',',')
# # data1 = data.strip(",")

# # print(data1)


# # filterdata = []
# # for x in query.split():
# # 	if x == 'exec':
# # 		pass
# # 	elif x != 'exec':
# # 		filterdata.append(x)
# # proc_name = filterdata[0]
# # data = filterdata[1:]
# # # print(data)

# # args_name = str(data).strip('[,]')

# # query = f"exec ap_get_rule 'F36DF97E-F80C-44C1-A64F-6BE5D07FD298',1"
# # filterdata = []
# # for x in query.split():
# # 	if x == 'exec':
# # 		pass
# # 	elif x != 'exec':
# # 		filterdata.append(x)
# # proc_name = filterdata[0]
# # # print(proc_name)
# # data = filterdata[1:]
# # # print(data)

# # args_name = ""
# # name = args_name.join(data)
# # print(name)
# def RemoveNonAscii(word):
#     if isinstance(word, str):
#         wordbytes = word.encode('ascii', 'ignore')
#         return wordbytes.decode().replace("'", "''")
#     return word

# def CompareDates(start, end, shutoff):
#     log.info("--Comparing dates...")

#     for i in [start, end, shutoff]:
#         if not isinstance(i, str):
#             log.error(f"--{i} is not string")
#             return False
#     if len(start) == 0 and len(end) == 0 and len(shutoff) == 0:
#         return {
#             "Start": "",
#             "End": "",
#             "Shutoff": ""
#         }

#     try:
#         StartDate = datetime.fromisoformat(start).date()
#         EndDate = datetime.fromisoformat(end).date()
#         ShutoffDate = datetime.fromisoformat(shutoff).date()
#     except ValueError as e:
#         log.error(f"--{e}")
#         return False
#     else:
#         if ((StartDate > EndDate) or (StartDate > ShutoffDate) or (ShutoffDate > EndDate)):
#             log.error(
#                 "--Start Date is greater than EndDate/shutoffdate")
#             return False

#         log.info("--Dates are OK")
#         return {
#             "Start": f"{datetime.fromisoformat(f'{StartDate}T00:01:00')}",
#             "End": f"{datetime.fromisoformat(f'{EndDate}T23:59:00')}",
#             "Shutoff": f"{datetime.fromisoformat(f'{ShutoffDate}T23:59:00')}"
#         }


# body = {
#     "name": "Nitesh",
#     "ruletype": 4,
#     "subruletype": 13,
#     "stores": [
#         "1",
#         "9",
#         "103"
#     ],
#     "iselastic": 1,
#     "bankOffer": 0,
#     "suggestedOffer": 0,
#     "suggestedOfferCount": 1,
#     "createOffer": 1,
#     "nooffer": 0,
#     "criteria": {
#         "in_last_days": 90,
#         "times_purchased": 0,
#         "max_times_purchased": 0,
#         "amount_spend": 1,
#         "max_amount_spend": 1,
#         "TopNshoppers": "0",
#         "zip_codes": [],
#         "departments": [
#             "1",
#             "4",
#             "5"
#         ],
#         "upcs": [],
#         "visits_containing_upcs": 1,
#         "max_visits_containing_upcs": 1
#     },
#     "coupon": [
#         {
#             "name": "test coupon",
#             "frequency": "daily",
#             "offertype": 1,
#             "offerstart": 1,
#             "minamount": "0",
#             "minquantity": 1,
#             "reward_min_quantity": 1,
#             "rewardamount": "0.01",
#             "isdiscountpercentage": 0,
#             "purchaseupcs": [],
#             "rewardupcs": [],
#             "stores": [],
#             "departments": [],
#             "expireprevcoupon": 0,
#             "isdow": 0,
#             "coupon_limit": 1,
#             "isfeaturecoupon": 0,
#             "includeinweeklyemail": 0,
#             "validityindays": 7,
#             "coupon_start_time": "00:00",
#             "coupon_end_time": "23:59",
#             "sendpushnotification": 0,
#             "message": "",
#             "time": "08:00",
#             "postfb": 0,
#             "fbmessage": "",
#             "fbtime": "09:00",
#             "sendsms": 0,
#             "smsmessage": "",
#             "smstime": "10:00",
#             "sendemail": 0,
#             "emailmessage": "",
#             "emailtime": "11:00"
#         }
#     ],
#     "schedule": {
#         "frequency": "daily",
#         "startdate": "2023-01-21",
#         "enddate": "2023-02-11",
#         "email": "admin@gmail.com",
#         "approvalrequired": 1,
#         "notifyadminpostrun": 1,
#         "groupstatsupdate": 1,
#         "notifysuggestedoffers": 1
#     },
#     "notifications": []
# }

# dates = CompareDates(body['schedule']['startdate'],
#                          body['schedule']['enddate'], body['schedule']['enddate'])

# query = f"exec ap_update_rule '', {RemoveNonAscii(body['ruletype'])},'{RemoveNonAscii(body['name'])}', '{RemoveNonAscii(body['subruletype'])}', {body['nooffer']}, '{RemoveNonAscii(body['schedule']['frequency'])}','{dates['Start']}', '{dates['End']}', '{RemoveNonAscii(body['schedule']['email'])}', {body['schedule']['approvalrequired']}, {body['iselastic']}, {body['schedule']['notifyadminpostrun']},{body['schedule']['notifysuggestedoffers']}, {body['schedule']['groupstatsupdate']},{clientId}, '{clientGuid}', 1, {UID}"

ajay = [
    {
        "countryname": "Canada",
        "capitalname": "Ottawa",
        "flagimage": "/flag/canada.gif"
    },
    {
        "countryname": "China",
        "capitalname": "Beijing",
        "flagimage": "/flag/china.gif"
    },
    {
        "countryname": "France",
        "capitalname": "Paris",
        "flagimage": "/flag/france.gif"
    },
    {
        "countryname": "Germany",
        "capitalname": "Berlin",
        "flagimage": "/flag/germany.gif"
    },
    {
        "countryname": "Hungary",
        "capitalname": "Budapest",
        "flagimage": "/flag/hungry.gif"
    },
    {
        "countryname": "India",
        "capitalname": "New Delhi",
        "flagimage": "/flag/india.gif"
    },
    {
        "countryname": "Indonesia",
        "capitalname": "Jakarta",
        "flagimage": "/flag/indonesia.gif"
    },
    {
        "countryname": "Iran",
        "capitalname": "Tehran",
        "flagimage": "/flag/iran.gif"
    },
    {
        "countryname": "Iraq",
        "capitalname": "Baghdad",
        "flagimage": "/flag/iraq.gif"
    },
    {
        "countryname": "Bhutan",
        "capitalname": "Thimphu",
        "flagimage": "/flag/bhutan.gif"
    },
    {
        "countryname": "Afghanistan",
        "capitalname": "Kabul",
        "flagimage": "/flag/afghanistan.gif"
    },
    {
        "countryname": "Bangladesh",
        "capitalname": "Dhaka",
        "flagimage": "/flag/bangladesh.gif"
    },
    {
        "countryname": "Japan",
        "capitalname": "Tokyo",
        "flagimage": "/flag/japan.gif"
    },
    {
        "countryname": "Malaysia",
        "capitalname": "Kuala Lumpur",
        "flagimage": "/flag/malaysia.gif"
    },
    {
        "countryname": "Mauritius",
        "capitalname": "Port Louis",
        "flagimage": "/flag/mauritius.gif"
    },
    {
        "countryname": "Nepal",
        "capitalname": "Kathmandu",
        "flagimage": "/flag/nepal.gif"
    },
    {
        "countryname": "Netherlands",
        "capitalname": "Amsterdam",
        "flagimage": "/flag/netherland.gif"
    },
    {
        "countryname": "New Zealand",
        "capitalname": "Wellington",
        "flagimage": "/flag/newzealand.gif"
    }
]
