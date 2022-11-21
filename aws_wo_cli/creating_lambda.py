import boto3


client = boto3.client('lambda')

with open('C:\\Users\\rsa-l\\Desktop\\vs py code\\index.zip',"rb") as data:
    buf = data.read()


response = client.create_function(
    FunctionName ='funcwoaws',
    Runtime='python3.8',
    Role='arn:aws:iam::206239526750:role/lamdawithoutapi-HelloWorldFunctionRole-1EF026WNGMI2M',
    Handler='index.lambda_handler',
    Code={
        'ZipFile':buf,
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