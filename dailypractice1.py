# import requests
# import os
import numpy as np
import json
# conn = os.environ.get("API")
# guid = 'F36DF97E-F80C-44C1-A64F-6BE5D07FD298'
# UID = 1
# RuleId = 1

# query = f"exec ap_get_rule '{guid}', {UID}"
# query = f"exec ap_get_rule_stores {RuleId}"

# def Accessdbdata(conn,query):

# 	try:
# 		filterdata = []
# 		for x in query.split():
# 			if x == 'exec':
# 				pass
# 			elif x != 'exec':
# 				filterdata.append(x)
# 		proc_name = filterdata[0]
# 		data = filterdata[1:]

# 		name = ""
# 		args_name = name.join(data)

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

# event = {
#     "AccountId": "",
#     "FIRSTNAME": "NITESH",
#     "LASTNAME": "YADAV",
#     "MOBILENUMBER": 9110514052,
#     "EMAIL": "abc@gmail.com",
#     "ADDRESS": "manikonda",
#     "PIN": 1604
# }

# data = json.dumps(event)
# body = json.loads(data)


# cursor.execute(
#     f"exec update_bank_data @AccountId='', @FIRSTNAME='{body['FIRSTNAME']}', @LASTNAME='{body['LASTNAME']}', @MOBILENUMBER={body['MOBILENUMBER']}, @EMAIL = '{body['EMAIL']}',@ADDRESS='{body['ADDRESS']}',@PIN = {body['PIN']}")
# conn.commit()

# def AccessDBData(conn, query):
#     cursor = conn.cursor(as_dict=True)
#     log.info(f"--Running query - {query}")
#     try:
#         # cursor.execute("update brand set name = 'McD' OUTPUT inserted.id where company_id = 2;")
#         cursor.execute(f"{query};")
#         row = cursor.fetchall()
#         if cursor.rowcount > 0:
#             conn.commit()
#             log.info(f"--Query results - {row}")
#             # row is list of results(json)
#             return row
#         return []
#     except pymssql.OperationalError as e:
#         log.error(f"--DB insertion/update/delete Error - {e}")
#         return False
#     except pymssql.Error as e:
#         log.error(f"--DB insertion/update/delete Error - {e}")
#         cursor.execute("ROLLBACK;")
#         conn.rollback()
#         return False

# import boto3
# import requests

# msg = list(map(int, ("10", "20", "30", "40", "50")))
# # print(msg)


# response1 = requests.get(
#     " https://0jpo6xtx8k.execute-api.ap-south-1.amazonaws.com/data/employee_results")
# data = response1.text


# result = json.loads(data)
# body_data = result['body']['employeeids']
# # print(body_data)

# final_res = list(map(dict, body_data))


# def body(final_res):

#     qname = 'first_queue'
#     store = boto3.client('sqs')
#     response = store.send_message(
#         QueueUrl=f'https://sqs.ap-south-1.amazonaws.com/206239526750/{qname}',
#         MessageBody=json.dumps(final_res),
#     )

#     return (response)


# # print(body(final_res))

# for res in final_res:
#     if isinstance(res, dict):
#         result = body(res)

# data = (200, 150)
# data1 = []
# if data[0] == 200:
#     data1.append(data[1])
# print(data1)


# def AddmultipleCoupons(event):
#     log.info("--------------- Method Start - Add Multiple Coupons----------------")
#     body = json.loads(event["body"])

#     coupons = body["Coupon"]
#     MCoup = []
#     for i in coupons:
#         data = AddCoupon(i)
#         if data[0] == 200:
#             MCoup.append(data[1])
#         else:
#             return returnValue(400, "something went wrong.")
#     return returnValue(200, data)
import string
import random
letters = string.ascii_lowercase
Numbers = string.digits
# Random_Num = ''.join(random.choice(Numbers) for _ in range(24))
# print(Random_Num)
random_num = []
for i in range(10):
    random_num.append(''.join(random.choice(Numbers)))


num = ''.join(random.choice(Numbers)for _ in range(10))
print(num)