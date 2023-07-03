import boto3


client = boto3.client('lambda')

with open('C:\\Users\\rsa-l\\Desktop\\vs py code\\index.zip', "rb") as data:
    buf = data.read()


response = client.create_function(
    FunctionName='funcwoaws',
    Runtime='python3.8',
    Role='arn:aws:iam::206239526750:role/lamdawithoutapi-HelloWorldFunctionRole-1EF026WNGMI2M',
    Handler='index.lambda_handler',
    Code={
        'ZipFile': buf,
    },
    Description='function creation without cli',
    Timeout=15,
    MemorySize=128,
    Publish=True,
    TracingConfig={
        'Mode': 'Active',
    },
    PackageType='Zip',
    Architectures=[
        'x86_64'
    ],
)


print(response)

# Get the existing Lambda function ARN
# existing_lambda_arn = '<existing_lambda_arn>'
# get_existing_lambda_response = lambda_client.get_function(
#     FunctionName=existing_lambda_arn)
# existing_lambda_role_arn = get_existing_lambda_response['Configuration']['Role']

# # Create a new Lambda function with the existing role ARN
# # response = lambda_client.create_function(
# #     FunctionName='<new_lambda_function_name>',
# #     Runtime='python3.8',
# #     Role=existing_lambda_role_arn,
# #     Handler='lambda_function.lambda_handler',
# #     Code={
# #         'S3Bucket': '<s3_bucket_name>',
# #         'S3Key': '<s3_key>'
# #     }
# # )

# print(existing_lambda_role_arn)
