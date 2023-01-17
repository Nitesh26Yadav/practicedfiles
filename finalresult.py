import requests
import os

conn = os.environ.get("API")
guid = 'F36DF97E-F80C-44C1-A64F-6BE5D07FD298'
UID = 1
RuleId = 1

query = f"exec ap_get_rule '{guid}', {UID}"
query = f"exec ap_get_rule_stores {RuleId}"

def Accessdbdata(conn,query):  

	try:
		filterdata = []
		for x in query.split():
			if x == 'exec':
				pass
			elif x != 'exec':
				filterdata.append(x)
		proc_name = filterdata[0]
		data = filterdata[1:]

		name = ""
		args_name = name.join(data)

		body = {

		"Instance":"veritra",

		"DB":"RSA_CentMark",

		"Proc": proc_name,

		"Args": args_name
	
		}

		response = requests.post(conn,json = body)
		# print(proc_name)
		# print(args_name)

		rules = response.json()
		return rules['Message']

	except:
		return False

data = Accessdbdata(conn,query)
print(data)
