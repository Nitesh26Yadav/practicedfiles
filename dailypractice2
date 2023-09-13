# import requests
# import os

# # conn = "https://0ry7jslpr3.execute-api.us-east-1.amazonaws.com/dev/rule"
# # conn = "https://pfmfnfh7lrtqicmjeu4nmswqui0ikdwa.lambda-url.us-east-1.on.aws/query"
# query = "exec ap_get_rule_top_n_shoppers 0"
# guid = 'F36DF97E-F80C-44C1-A64F-6BE5D07FD298'
# UID = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VySUQiOjEwMSwiaXNfY29uc2VudF9wcm92aWRlZCI6dHJ1ZSwidXNlcm5hbWUiOiJkZW1vdXNlckBhdXRvcGlsb3QuY29tIiwidXNlcl9ndWlkIjoiN0UyOTExMDUtRDQyNy00QTRDLThGOEMtMUE5MUFCOUY3QTMzIiwiZmlyc3RfbmFtZSI6IkpvaG4iLCJsYXN0X25hbWUiOiJGYXJtcyIsInJldGFpbGVyIjp7ImlkIjo0OCwic2NvcGVzIjpbXX0sImV4cGlyZXNfaW4iOiIyMDIyLTAzLTA1IDE4OjQ3OjIzLjQyMjI2MCJ9.EhC9HR6vgi0dqmD24TpDpe4FEee1VT4p311zHACDk8k'

# # query = f"exec ap_get_rule {guid}, {UID}"
# # conn = os.environ.get("API")
# # data = []
# # for x in query.split():
# # 	if x == 'exec':
# # 			pass
# # 	elif x != 'exec':
# # 			data.append(x)


# def Accessdbdata(conn, query):
#     conn = os.environ.get("API")
#     try:
#         filterdata = []
#         for x in query.split():
#             if x == 'exec':
#                 pass
#             elif x != 'exec':
#                 filterdata.append(x)
#         proc_name = filterdata[0]
#         data = filterdata[1:]

#         args_name = str(data).replace('[', '').replace(']', '')

#         body = {

#             "Instance": "veritra",

#             "DB": "RSA_CentMark",

#             "Proc": proc_name,

#             "Args": args_name

#         }
#         response = requests.post(conn, json=body)

#         if not response:
#             data = []
#             for x in query.split():
#                 if x == 'exec':
#                     pass
#                 elif x != 'exec':
#                     data.append(x)

#             Gui = data[1]
#             idi = data[2]

#             headers = {

#                 'Authorization': idi
#             }
#             response = requests.get(f'{conn}/{Gui}', headers=headers)

#         rules = response.json()
#         return rules['Message']

#     except:
#         return False


# data = Accessdbdata(conn="https://pfmfnfh7lrtqicmjeu4nmswqui0ikdwa.lambda-url.us-east-1.on.aws/query",
#                     query=f"exec ap_get_rule {guid}, {UID}")

# # data = Accessdbdata(conn = "https://0ry7jslpr3.execute-api.us-east-1.amazonaws.com/dev/rule",query = f"exec ap_get_rule {guid}, {UID}" )
# print(data)

data = [
    {
        "web_pages": [
            "https://www.upes.ac.in/"
        ],
        "alpha_two_code": "IN",
        "state-province": "Dehradun",
        "country": "India",
        "domains": [
            "upes.ac.in"],
        "name": "University of Petroleum and Energy Studies",
        "id": "1"

    },
    {
        "web_pages": [
            "http://www.davietjal.org/"
        ],
        "alpha_two_code": "IN",
        "state-province": "Punjab",
        "country": "India",
        "domains": [
            "davietjal.org"
        ],
        "name": "DAV Institute of Engineering & Technology",
        "id": "2"

    },
    {
        "web_pages": [
            "http://www.lpu.in/"
        ],
        "alpha_two_code": "IN",
        "state-province": "Punjab",
        "country": "India",
        "domains": [
            "lpu.in"
        ],
        "name": "Lovely Professional University",
        "id": "3"
    }
]
x_data = []
for i in data:
    domain_data = i['domains'][0]
    name = i['state-province']
    id = int(i['id'])
    # print(i)
    x_data = domain_data
    print(id, type(id))
