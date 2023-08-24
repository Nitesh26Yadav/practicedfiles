import boto3
import os
client = boto3.client('apigateway')


AccID = os.environ.get('AccID')
# Creating RestApi:-

'''
rest_api = client.create_rest_api(
    name='api name')
print(rest_api)
rest_api_id = rest_api["id"]
print(rest_api_id)
'''

# Get RestApi's root id:

rest_api_id = 'yfhscgmmu3'
root_resource_id = client.get_resources(
    restApiId=rest_api_id
)['items'][0]['id']
# print(root_resource_id)


# Creating an Api resource:-
parent_id = 'add parent id'
FuncName = 'function name'

# api_resource = client.create_resource(
#     restApiId=rest_api_id,
#     parentId=parent_id,
#     pathPart='getsearchresult')
# print(api_resource)

# api_resource_id = api_resource['id']
# print(api_resource_id)

api_resource_id = '57q7x8'
# Adding a GET method to the rest api resource:-

# api_method = client.put_method(
#     restApiId=rest_api_id,
#     resourceId=api_resource_id,
#     httpMethod='GET',
#     authorizationType='NONE'
# )
# print(api_method)

# put_method_response = client.put_method_response(
#     restApiId=rest_api_id,
#     resourceId=api_resource_id,
#     httpMethod='GET',
#     statusCode='200'
# )
# print(put_method_response)


# put_integration = client.put_integration(
#     restApiId=rest_api_id,
#     resourceId=api_resource_id,
#     httpMethod='GET',
#     type='AWS_PROXY',
#     integrationHttpMethod='POST',
#     uri=f'arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:{AccID}:function:{FuncName}/invocations')
# print(put_integration)

# '''-------putting integration responses-------'''
# put_integration_response = client.put_integration_response(
#     restApiId=rest_api_id,
#     resourceId=api_resource_id,
#     httpMethod='GET',
#     statusCode='200',
#     contentHandling='CONVERT_TO_BINARY' or 'CONVERT_TO_TEXT'
# )
# print(put_integration_response)

# # response = client.get_rest_api(
# #     restApiId=rest_api_id,
# # )

# #  Adding POST method to rest api resource:-
post_api_method = client.put_method(
    restApiId=rest_api_id,
    resourceId=api_resource_id,
    httpMethod='POST',
    authorizationType='NONE'
)
print(post_api_method)

put_method_response = client.put_method_response(
    restApiId=rest_api_id,
    resourceId=api_resource_id,
    httpMethod='POST',
    statusCode='200'
)
print(put_method_response)


put_integration = client.put_integration(
    restApiId=rest_api_id,
    resourceId=api_resource_id,
    httpMethod='POST',
    type='AWS_PROXY',
    integrationHttpMethod='POST',
    uri=f'arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:{AccID}:function:{FuncName}/invocations')
print(put_integration)

'''-------putting integration responses-------'''
put_integration_response = client.put_integration_response(
    restApiId=rest_api_id,
    resourceId=api_resource_id,
    httpMethod='POST',
    statusCode='200',
    contentHandling='CONVERT_TO_BINARY' or 'CONVERT_TO_TEXT'
)
print(put_integration_response)

response = client.create_deployment(
    restApiId=rest_api_id,
    stageName='data'
)

print(response)


# last step for Api gateway
# Lmbdaclient = boto3.client('lambda')

# pathPart = 'getsearchresult'

# AddPermission = Lmbdaclient.add_permission(

#     FunctionName=FuncName,

#     StatementId=f'{FuncName}-Permission-{pathPart}',

#     Action='lambda:InvokeFunction',

#     Principal='apigateway.amazonaws.com',

#     SourceArn=f'arn:aws:execute-api:us-east-1:{AccID}:{rest_api_id}/data/POST/{pathPart}'

# )
# print(AddPermission)
