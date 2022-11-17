import pymssql
import pandas as pd

conn = pymssql.connect(
            server='database-1.cxrjyosgnij0.ap-south-1.rds.amazonaws.com', 
            user='admin', 
            password='Veritra2022', 
            database='employeedata')

cursor = conn.cursor()


query=("select * from fooddata")

cursor.execute(query)
df = pd.read_sql(query,conn)
# print(df)


transaction = (df[(df['transaction_date_time_pt'] >= '2022-05-16 04:00:00') & (df['transaction_date_time_pt'] <= '2022-05-16 05:00:00')])


total = (transaction['transaction_amt'])

sum = 0
for num in total:
    sum = sum + num

print(round(sum,1))

