import pymssql
import pandas as pd

conn = pymssql.connect(
    server='database-1.cxrjyosgnij0.ap-south-1.rds.amazonaws.com',
    user='admin',
    password='Veritra2022',
    database='employeedata')


cursor = conn.cursor()
cursor.execute('''
                CREATE TABLE test(
                    userId int, 
                    id int, 
                    title nvarchar(200), 
                    body nvarchar(200),
                    )
                ''')

df = pd.read_csv(
    r'C:\Users\rsa-l\Desktop\vs py code\python (api,pandas,csv)\post.csv')
# print(df)

data1 = []

for row in df.itertuples():
    data1.append(row)
    # data2 = tuple(data1)


cursor.executemany(
    '''INSERT INTO test(userId,id,title,body) VALUES(%s,%s,%s,%s)''', tuple(data1))


conn.commit()
