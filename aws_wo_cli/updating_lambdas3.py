import boto3


client = boto3.client('lambda')

response =client.update_function_code(
    FunctionName ='func',
    Code={
        'S3Bucket': 'nitesh.practice',
        'S3Key': 'funcwosam.zip',
        
    },
)

# print(response)