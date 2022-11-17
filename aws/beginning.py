import boto3

aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("beginning.02")

response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
        },
)

print(response)