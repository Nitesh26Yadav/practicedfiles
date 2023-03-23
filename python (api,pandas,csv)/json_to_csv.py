import pandas as pd
import csv
import json
import requests


url = "https://okpricemart.grocerypundit.com/api/AogGetOrderDetailsToPOSFormat"
body = {
    "rsa_client_id": "181",
    "clientStoreId": "1",
    "member_number": "44674934368",
    "ecomOrderId": "24389"
}


def get_data(url, body):

    response = requests.post(url, json=body)
    rules = response.json()
    # result = rules['data']['order_items']
    result = rules['data']
    return result


data = get_data(url, body)
data1 = []

data1.append({
    "Transaction Date": "2023-02-02",
    "Transaction Time": "05:24:21",
    "Transaction ID": data["order_id"],
    "HDR": {
        "Version": "",
        "Organization": "",
        "Loyality": data["member_number"],
        "Tax ID": "",
        "Tax ID State Code": "",
        "Transaction Status": "",
        "": ""
    }})
for i in data['order_items']:
    data1.append({
        "Transaction Date": "2023-02-02",
        "Transaction Time": "05:24:21",
        "Transaction ID": data["order_id"],
        "UPC": {
            "Product Code": i['sku'],
            "Retail Type": "L",
            "Multiple": i['price'],
            "Price": i['price'],
            "Quantity": i['qty'],
            "Weight": i['weight'],
            "": ""
        }
    })
for i in data['getCouponList']:
    data1.append({
        "Transaction Date": "2023-02-02",
        "Transaction Time": "05:24:21",
        "Transaction ID": data["order_id"],
        "CPN": {
            "Coupon Type": "",
            "Coupon code": "",
            "Amount": "",
            "Dept Code": "",
            "field5": "",
            "field6": "",
            "field7": ""
        }
    })

data1.append({
    "Transaction Date": "2023-02-02",
    "Transaction Time": "05:24:21",
    "Transaction ID": data["order_id"],
    "TND": {
        "Media Code": data["payment_method_name"],
        "Account Number": "",
        "Tendered Amount": data["transaction_tax_amount"],
        "field4": "",
        "field5": "",
        "field6": "",
        "field7": ""
    }

})

data1.append({
    "Transaction Date": "2023-02-02",
    "Transaction Time": "05:24:21",
    "Transaction ID": data["order_id"],
    "TAX": {
        "Tax Code": "",
        "": "",
        "": "",
        "Tax Collected": data["transaction_tax_amount"],
        "field5": "",
        "field6": "",
        "field7": ""
    }
})
count = len(data1)


data1.append({
    "Transaction Date": "2023-02-02",
    "Transaction Time": "05:24:21",
    "Transaction ID": data["order_id"],
    "FTR": {
        "Detail Count": count-1,
        "": "",
        "Field3": "",
        "Tax Total": data["transaction_tax_amount"],
        "Transaction Total": data["transaction_total_amount"],
        "Field6": "",
        "Field7": ""
    }
})
# print(data1)
# for i in data1:
#     print(i)
json_data = json.dumps(data1)
# print(json_data)
'''
1)before orderitems starts
2)in data1 already hdr should be there
loop into order items to get upc data.
after complete loop
do one more loop to get how many coupons rows  are there
ask keyur to make payment in array[] - both are same.

ask him to get list of tender-both are same.
insert row tax - ask keyur
insert FTR

each row each json is a row in csv file.
'''
df = pd.read_json(json_data)
# print(df.columns)
df.columns = df.columns.str.replace(',', '|')

df.to_csv('file16.csv', sep='|', index=False)
print(df)
