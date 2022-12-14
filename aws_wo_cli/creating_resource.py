import boto3

client = boto3.client('apigateway')

'''--------creating resource to path------'''
# response = client.create_resource(
#     restApiId = "0jpo6xtx8k",
#     parentId='nn3tnn0doi',
#     pathPart='employee_results'
# )

'''------Adding methods------'''

response = client.put_method(
    restApiId = "0jpo6xtx8k",  
    resourceId='pfs44h',
    httpMethod='GET',
    authorizationType='None'
)


'''---------putting integration---------'''

response = client.put_integration(
    restApiId = "0jpo6xtx8k",
    resourceId='pfs44h',
    httpMethod='GET',
    type = 'AWS_PROXY',
    integrationHttpMethod='POST',
    uri = "arn:aws:apigateway:ap-south-1:lambda:path/2015-03-31/functions/arn:aws:lambda:ap-south-1:206239526750:function:databaseapi1/invocations"
)

'''-------putting integration responses-------'''
response = client.put_integration_response(
    restApiId = "0jpo6xtx8k",
    resourceId='pfs44h',
    httpMethod='GET',
    statusCode='200',
    contentHandling = 'CONVERT_TO_BINARY'or 'CONVERT_TO_TEXT'
)

'''-----------creating deployemnt-------------'''
response = client.create_deployment(
    restApiId="0jpo6xtx8k",
    stageName='data'
)

print(response)
