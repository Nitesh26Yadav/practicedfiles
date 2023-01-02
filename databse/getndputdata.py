import boto3
import pymssql
import pandas as pd

s3_client= boto3.client('s3',
        aws_access_key_id= "AKIATABGVN5PEF4BS5PR",
        aws_secret_access_key="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")



res = s3_client.put_object(
    Body = open('C:\\Users\\rsa-l\\Desktop\\vs py code\\python (api,pandas,csv)\\rpt.599.food_bazaar.in_store_transactions.v2.2022-05-16.24380053.csv','r').read(),
    Bucket = 'nitesh.practice',
    Key = 'foodstore.csv'
)

# print(res)

resi = s3_client.get_object(
    Bucket = 'nitesh.practice',
    Key = 'foodstore.csv'
)
# print(resi)

# data = resi.get("Body").read().decode()
# file = open("foodstore.csv","w",index = False)
# file.writelines(data)
# file.close()
# print(file)



df = pd.read_csv(r'C:\\Users\\rsa-l\\Desktop\\vs py code\\python (api,pandas,csv)\\foodstore.csv',index_col=False)

result1 = df.loc[df['store_location_code']==72]
# print(result1)
result2 = result1.dropna(how='all',axis=1)
result = result2.dropna(how ='any',axis=0)
# print(result)



conn = pymssql.connect(
            server='database-1.cxrjyosgnij0.ap-south-1.rds.amazonaws.com', 
            user='admin', 
            password='Veritra2022', 
            database='employeedata')

cursor = conn.cursor()
# cursor.execute('''
#                 CREATE TABLE foodStoredata(
#                     order_id float DEFAULT NULL,
#                     order_delivery_id float DEFAULT NULL,
#                     store_location_code INT DEFAULT NULL,
#                     store_zip_code INT DEFAULT NULL, 
#                     transaction_date_pt DATE DEFAULT NULL, 
#                     transaction_date_time_pt DATETIME DEFAULT NULL,
#                     transaction_amt float DEFAULT NULL, 
#                     approval_code INT DEFAULT NULL, 
#                     stan INT DEFAULT NULL
#                 )
#             ''')



data =[]
for row in result.itertuples():
    data.append(row[1:])
    
# print(data)

sql = ("INSERT INTO foodStoredata(order_id , order_delivery_id , store_location_code , store_zip_code , transaction_date_pt , transaction_date_time_pt , transaction_amt , approval_code , stan ) VALUES( %s , %s , %s , %s , %s , %s , %s , %s , %s )")

data = tuple(data)
# print(data)
finaldata = []
for each in data:
    finaldata.append(each)
    cursor.execute(sql,(each))

conn.commit()

# cursor.execute("select * from fooddata where transaction_date_time_pt between '2022-05-16 04:00:00' and '2022-05-16 05:00:00'")


# data1 = []
# for each in cursor:
#     data1.append(each)
# # print(data1)


# cursor.execute("select sum(transaction_amt) from fooddata where transaction_date_time_pt between '2022-05-16 04:00:00' and '2022-05-16 05:00:00'")


# data1=[]
# for total in cursor:
#     data1.append(total)

# print(data1)

# conn.commit()