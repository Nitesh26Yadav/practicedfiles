import boto3
import os.path
import logging
import json
import pandas as pd
import os

log = logging.getLogger()
log.setLevel(logging.INFO)


def returnValue(Code, Msg):
    log.info(f"API Response - {Msg}")
    log.info(
        "-------------------------END OF CODE------------------------------------")
    return {
        "statusCode": Code,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Methods': 'ANY'
        },
        "body": json.dumps(Msg)}


def lambda_handler(event, context):
    log.info(
        "--------------------------lambda_handler started--------------------------")
    log.info(f"event - {event}")
    if event['requestContext']['identity']['sourceIp'] != '52.86.137.172':
        return returnValue(404, "Access denied")
    data = json.loads(event['body'])
    if 'ftp_location' not in data:
        return returnValue(400, "bad request - ftp_location is requried")

    order_update = data["order_placed_on"].split()
    MFR = os.environ.get("MFRCouponDeptId")
    Store = os.environ.get("StoreCouponDeptId")

    data1 = [
        {
            "Transaction Date": order_update[0],
            "Transaction Time": order_update[1],
            "Transaction ID": data["order_id"],
            "Record Type": "HDR",
            "Field 1": "1",
            "Field 2": "AOG",
            "Field 3": f"{data['member_number']}",
            "Field 4": "",
            "Field 5": "",
            "Field 6": "",
            "Field 7": "",
        }
    ]
    # Adding UPC data.
    data1.extend(
        {
            "Transaction Date": order_update[0],
            "Transaction Time": order_update[1],
            "Transaction ID": data["order_id"],
            "Record Type": "UPC",
            "Field 1": int(i['sku']),
            "Field 2": "L",
            "Field 3": f"{i['qty']}",
            "Field 4": i['price'],
            "Field 5": i['qty'],
            "Field 6": i['weight'],
            "Field 7": "",
        }
        for i in data['order_items']
    )
    # Adding CPN data.
    data1.extend(
        {
            "Transaction Date": order_update[0],
            "Transaction Time": order_update[1],
            "Transaction ID": data["order_id"],
            "Record Type": "CPN",
            "Field 1": "V" if i["CouponCategoryId"] == 4 else "S",
            "Field 2": "",
            "Field 3": f"{i['new_discount']}",
            "Field 4": MFR if i["CouponCategoryId"] == 4 else Store,
            "Field 5": "",
            "Field 6": "",
            "Field 7": "",
        }
        for i in data['getCouponList']
    )
    data1.extend(
        (
            {
                "Transaction Date": order_update[0],
                "Transaction Time": order_update[1],
                "Transaction ID": data["order_id"],
                "Record Type": "TND",
                "Field 1": "",
                "Field 2": "",
                "Field 3": f"{data['transaction_total_amount']}",
                "Field 4": "",
                "Field 5": "",
                "Field 6": "",
                "Field 7": "",
            },
            {
                "Transaction Date": order_update[0],
                "Transaction Time": order_update[1],
                "Transaction ID": data["order_id"],
                "Record Type": "TAX",
                "Field 1": "1",
                "Field 2": "",
                "Field 3": f"{data['subtotal_amount']}",
                "Field 4": data["transaction_tax_amount"],
                "Field 5": "",
                "Field 6": "",
                "Field 7": "",
            },
        )
    )
    count = len(data1)
    # Adding FTR data.
    data1.append({
        "Transaction Date": order_update[0],
        "Transaction Time": order_update[1],
        "Transaction ID": data["order_id"],
        "Record Type": "FTR",
        "Field 1": int(count-1),
        "Field 2": "",
        "Field 3": f"{data['subtotal_amount']}",
        "Field 4": data["transaction_tax_amount"],
        "Field 5": data["transaction_total_amount"],
        "Field 6": "",
        "Field 7": ""
    }
    )

    json_data = json.dumps(data1)

    df = pd.read_json(json_data, dtype={"Field 3": "int64"})  # type: ignore
    df.columns = df.columns.str.replace(',', '|')

    # converting dataframe to csv file.
    df = df.to_csv(sep='|', index=False, header=False)
    file_name = df.encode('utf-8')

    # Adding file into S3 Bucket
    s3 = boto3.client('s3')
    if response := s3.put_object(
        Body=file_name,
        Bucket=os.environ.get("BUCKET"),
        Key=f"aog/aogecom/clients/{data['ftp_location']}/orders/{data['order_number']}.csv",
    ):
        log.info("file uploaded")
        return returnValue(200, {"Message": "Order Injected", "FileLocation": f"aog/aogecom/clients/{data['ftp_location']}/orders/{data['order_number']}.csv"})

    log.error("file is not uploaded")
    return returnValue(400, {"Message": "Order Injection Failed"})

# lambda_handler(event=url)
