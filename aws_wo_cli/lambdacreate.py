import boto3
import os

client = boto3.client('lambda')

# with open('C:add path', "rb") as data:
#     func = data.read()

# create_lambda = client.create_function(
#     FunctionName="add function name",
#     Runtime='python3.8',
#     Role='add role',
#     Handler='app.lambda_handler',
#     Code={"ZipFile": func},
#     Timeout=15,
#     MemorySize=128,
#     Publish=True,
#     Environment={
#         'Variables': {
# ''
#         }
#     },
#     TracingConfig={
#         'Mode': 'PassThrough',
#     },
#     Layers=[
#         'add layers',
#     ],
#     PackageType='Zip',
#     Architectures=[
#         'x86_64',
#     ]
# )
# print(create_lambda)

#  updating lambda function
# response = client.update_function_configuration(
#     FunctionName='existing function name',
#     Environment={
#         'Variables': {
#             ''
#         }
#     },
#     Layers=[
#         '',
#     ]
# )
# print(response)
# response = client.update_function_code(
#     FunctionName='function name to update',
#     ZipFile=func
# )
# print(response)


# existing_lambda_arn = 'add lambda function arn.'
# get_existing_lambda_response = client.get_function(
#     FunctionName=existing_lambda_arn)
# existing_lambda_role_arn = get_existing_lambda_response
# print(get_existing_lambda_response)


# deleting function:-
# response = client.delete_function(
#     FunctionName='RSA_dummy_lambda_func'
# )
# print(response)


# def SendQMsg(Msg, QName):
#     log.info(Msg)
#     ID = str(os.environ.get('ID')) # always use in varibales do not use in code.
#     try:
#         s3 = boto3.client('sqs')
#         response = s3.send_message(
#             QueueUrl=f"https://sqs.us-east-1.amazonaws.com/{ID}/{QName}",
#             MessageBody=json.dumps(Msg))
#         log.info(response)

#     except Exception as e:
#         log.info(e)
#         return [False, f"{e}"]
#     return [True, response['MessageId']]