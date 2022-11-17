import pymssql
import pandas as pd



conn = pymssql.connect(
            server='database-1.cxrjyosgnij0.ap-south-1.rds.amazonaws.com', 
            user='admin', 
            password='Veritra2022', 
            database='employeedata'
)

cursor = conn.cursor()
cursor.execute("select * from fooddata")

# data = []
# for row in cursor:
#     data.append(row)

# # data1 = str(data)
# print(data)

# data2 = pd.DataFrame(data)
# data2.to_csv('dbtest.csv',index=False)
