import boto3
import os.path

s3_client= boto3.client('s3',
        aws_access_key_id= "AKIATABGVN5PEF4BS5PR",
        aws_secret_access_key="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")

#creation of bucket

#res = s3_client.create_bucket(
#    Bucket = 'training.00',
#    CreateBucketConfiguration = {
#        'LocationConstraint':'ap-south-1'
#    }
#)
#print(res)

#upload file in bucket


# resi = s3_client.put_object(
#     Body = open('C:\\Users\\rsa-l\\Desktop\\vs py code\\aws.py\\dict2.py','r').read(),
#     Bucket = 'training.00',
#     Key = 'dictionary.2'
# )
# resi_status= resi.get('ResponseMetadata',{}).get('HTTPStatusCode')
# #print(resi_status)

# time={}
# time['evening'] = ['6:12'] 
# resi['time'] = time
# print(resi)

# res1 = (resi.pop('time'))
# print(resi)

