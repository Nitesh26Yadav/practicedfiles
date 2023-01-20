import requests
import os
from datetime import datetime
import logging
import json

log = logging.getLogger()
log.setLevel(logging.INFO)

guid = 'D3D099BE-A9DA-4924-A5BF-9ABC644F29BF'
UID = 1
RuleId = 1
RuleGuid = 'D3D099BE-A9DA-4924-A5BF-9ABC644F29BF'
# clientId = 1
# clientGuid =  '0C2BCC44-5C2B-4904-8B3F-755C57B488BC'

# query = f"exec ap_get_rule_criteria {RuleId}"
# db = os.environ.get("DB")
# instance = os.environ.get("Instance")

def ConnectDB():
	try:
		conn = os.environ.get("API")
		return conn
	except:
		return ("Something went wrong in Api")



def AccessDBData(conn,query):  
	db = os.environ.get("DB")
	instance = os.environ.get("Instance")
	try:
		filterdata = query.split()
		exec_name = filterdata[0]
		
		name = ""
		if exec_name == 'exec':
			proc_name = filterdata[1]
			args_name = name.join(filterdata[2:])

		elif exec_name != 'exec':
			proc_name = filterdata[0] 
			args_name = name.join(filterdata[1:])
			
		proc = proc_name
		args = args_name
		
		body = {

			"Instance":instance,

			"DB":db,

			"Proc": proc,

			"Args": args
	
		}
        
		response = requests.post(conn,json = body)

		rules = response.json()
		return rules['Message']

	except:
		return False

# print(Accessdbdata(conn,query))
# print(instance)
# print(db)