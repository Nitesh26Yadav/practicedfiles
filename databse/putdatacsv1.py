import io
import pymssql
import pandas as pd
import boto3



s3_client= boto3.client('s3',
        aws_access_key_id= "AKIATABGVN5PEF4BS5PR",
        aws_secret_access_key="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")

conn = pymssql.connect(
            server='database-1.cxrjyosgnij0.ap-south-1.rds.amazonaws.com', 
            user='admin', 
            password='Veritra2022', 
            database='employeedata'
)

cursor = conn.cursor()
cursor.execute("select * from test")



data = []
for row in cursor:
    data.append(row)

data1 = str(data)

file = pd.DataFrame(data)
file.to_csv('dbtest.csv',index=None)

a = file.set_index(0)
finaldata = str(a)

result = io.BytesIO(bytes(finaldata,'utf-8'))

res = s3_client.put_object(
    Body = result,
    Bucket = 'nitesh.practice',
    Key = 'dbtest3.csv'
)
print(res)
