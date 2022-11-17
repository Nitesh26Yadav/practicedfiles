import boto3


with open('C:\\Users\\rsa-l\\Desktop\\vs py code\\index.zip',"rb") as data:
    buf = (data.read())



client = boto3.client('lambda')

response = client.update_function_code(
    FunctionName='func',
    ZipFile = buf
)

# print(response)













# response = client.update_function_configuration(
#             FunctionName='func',
#             Environment={
#                 'Variables': {
#                     'key1': 'func'
#                 }
#             }
#         )
# print(response)