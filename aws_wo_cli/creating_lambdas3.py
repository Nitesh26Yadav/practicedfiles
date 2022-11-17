import boto3

client = boto3.client('lambda')


response = client.create_function(
    FunctionName ='func',
    Runtime='python3.8',
    Role='arn:aws:iam::206239526750:role/lamdawithoutapi-HelloWorldFunctionRole-1EF026WNGMI2M',
    Handler='index.lambda_handler',
    Code={
        'S3Bucket': 'nitesh.practice',
        'S3Key': 'funcwosam.zip',
        
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


# print(response)