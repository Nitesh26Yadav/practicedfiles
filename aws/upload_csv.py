import boto3
import os.path
import requests
import json
import pandas as pd
import os
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

url = "https://okpricemart.grocerypundit.com/api/AogGetOrderDetailsToPOSFormat"


def returnValue(Code, Msg):
    log.info(f"API Response - {Msg}")
    log.info(
        "--------------------------------END OF CODE --------------------------------")
    return {
        "statusCode": Code,
        "headers": {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'ANY'
        },
        "body": json.dumps(Msg)}


def lambda_handler(event, context):
    log.info(
        "------------------------------lambda_handler started------------------------")
    log.info(f"event-{event}")
    if event['requestContext']['identity']['sourceIp'] != '52.86.137.172':
        return returnValue(404, "Access denied")
    data = json.loads(event['body'])
    if 'ftp_location' not in data:
        return returnValue(400, "bad request - ftp_location is requried")

    data1 = []
    order_update = data["order_placed_on"].split()
    MFR = os.environ.get("MFRCouponDeptId")
    Store = os.environ.get("StoreCouponDeptId")

    # Adding HDR data.
    data1.append({
        "Transaction Date": order_update[0],
        "Transaction Time": order_update[1],
        "Transaction ID": data["order_id"],
        "Record Type": "HDR",
        "Field 1": "",
        "Field 2": "",
        "Field 3": int(data["member_number"]),
        "Field 4": "",
        "Field 5": "",
        "Field 6": "",
        "Field 7": ""
    })
    # Adding UPC data.
    for i in data['order_items']:
        data1.append({
            "Transaction Date": order_update[0],
            "Transaction Time": order_update[1],
            "Transaction ID": data["order_id"],
            "Record Type": "UPC",
            "Field 1": int(i['sku']),
            "Field 2": "L",
            "Field 3": i['price'],
            "Field 4": i['price'],
            "Field 5": i['qty'],
            "Field 6": i['weight'],
            "Field 7": i['final_price']
        }
        )

    # Adding CPN data.
    for i in data['getCouponList']:
        data1.append({
            "Transaction Date": order_update[0],
            "Transaction Time": order_update[1],
            "Transaction ID": data["order_id"],
            "Record Type": "CPN",
            "Field 1": "V" if i["CouponCategoryId"] == 4 else "S",
            "Field 2": "",
            "Field 3": i["new_discount"],
            "Field 4": MFR if i["CouponCategoryId"] == 4 else Store,
            "Field 5": "",
            "Field 6": "",
            "Field 7": ""
        }
        )
    # Adding TND data.
    data1.append({
        "Transaction Date": order_update[0],
        "Transaction Time": order_update[1],
        "Transaction ID": data["order_id"],
        "Record Type": "TND",
        "Field 1": data["payment_method_name"],
        "Field 2": "",
        "Field 3": data["transaction_tax_amount"],
        "Field 4": "",
        "Field 5": "",
        "Field 6": "",
        "Field 7": ""

    })
    # Adding TAX data.
    data1.append({
        "Transaction Date": order_update[0],
        "Transaction Time": order_update[1],
        "Transaction ID": data["order_id"],
        "Record Type": "TAX",
        "Field 1": "",
        "Field 2": "",
        "Field 3": "",
        "Field 4": data["transaction_tax_amount"],
        "Field 5": "",
        "Field 6": "",
        "Field 7": ""
    }
    )
    count = len(data1)
    for i in data['getCouponList']:
        new_discount = i['new_discount']
    # Adding FTR data.
    data1.append({
        "Transaction Date": order_update[0],
        "Transaction Time": order_update[1],
        "Transaction ID": data["order_id"],
        "Record Type": "FTR",
        "Field 1": int(count-1),
        "Field 2": "",
        "Field 3": data['sub_total_without_discount_amount'],
        "Field 4": data["transaction_tax_amount"],
        "Field 5": data["transaction_total_amount"],
        "Field 6": "",
        "Field 7": ""
    }
    )

    json_data = json.dumps(data1)
    print(json_data)
    # df = pd.read_json(json_data)
    # df.columns = df.columns.str.replace(',', '|')

    # # converting dataframe to csv file.
    # df = df.to_csv(sep='|', index=False, header=False)
    # file_name = df.encode('utf-8')

    # # Adding file into S3 Bucket
    # s3 = boto3.client("s3")
    # response = s3.put_object(
    #     Body=file_name,
    #     Bucket="beginning.00",
    #     Key="ftp_file_coupon.csv")

    # if response:
    #     print("file uploaded")
    # else:
    #     print("file is not uploaded")


lambda_handler(event=url)
