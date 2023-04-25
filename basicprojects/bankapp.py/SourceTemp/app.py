import logging
import json
from datetime import date, datetime
from CommonApis import DecodeJWT
from bankapi import Createuser

today = date.today()


log = logging.getLogger()
log.setLevel(logging.INFO)


def Response(HttpCode, Msg):
    log.info(f"-- Api Response --{Msg}")

    return {
        "StatusCode": HttpCode,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
        },
        "body": json.dumps({Msg})
    }

# import random
# import string


# def Createuser():
#     form = []
#     while True:
#         First_Name = input("Enter Your First Name here: ")
#         if First_Name.isalpha():
#             form.append(First_Name)
#             break
#         else:
#             print("Please Enter Valid Name")

#     while True:
#         Last_Name = input("Enter Your Last Name here: ")
#         if Last_Name.isalpha():
#             form.append(Last_Name)
#             break
#         else:
#             print("Please Enter Valid Name")

#     while True:
#         mobile_Number = input("Enter Your phone Number: ")
#         if mobile_Number.isdigit():
#             # mobile_Number = int(mobile_Number)
#             if len(mobile_Number) == 10:
#                 mobile_Number = int(mobile_Number)
#                 form.append(mobile_Number)
#                 break
#             else:
#                 print("please Enter 10 digits.")
#         else:
#             print("Please enter Correct Details.")
#     while True:
#         email_id = input("Enter Your Email id: ")
#         if email_id.endswith("gmail.com"):
#             form.append(email_id)
#             break
#         else:
#             print("Please enter valid Email id ends with ('@gmail.com')")
#     while True:
#         Address = input("Enter Your Address here: ")
#         if not Address:
#             print("Please Enter details.")
#         elif len(Address) < 10:
#             print("Please Enter valid details.")
#         else:
#             form.append(Address)
#             break
#     while True:
#         Password = input("Enter Your Password in digits: ")
#         if Password.isdigit():
#             if len(Password) < 4:
#                 print("Please Enter Aleast Four")
#                 Password = input("Enter Password in digits: ")
#             Re_Enter_Password = input("Enter Your Password Again: ")
#             if Password == Re_Enter_Password:
#                 form.append(Password)
#                 break
#             else:
#                 print("Please check your pin. \n It should Match Your Pin.")
#         else:
#             print("Please Enter Valid digit.")

#     return form


# user_details = Createuser()


# def deposit():
#     Account_details = []
#     while True:
#         AccountType = input(
#             "Choose '1' for Saving Account and '2' for Current Account: ")
#         if (AccountType != '1') and (AccountType != '2'):
#             print("please enter Valid Number 1 or 2.")
#         else:
#             if AccountType == '1':
#                 print("Thank You! For Choosing Saving Account.")
#             elif AccountType == '2':
#                 print("Thank You! For Choosing Current Account.")

    # AccountNo = ''.join(random.choice(string.digits)
    #                     for _ in range(16))

#             print("Your Account Number: " + AccountNo)
#             break

#     while True:
#         amount = input("please enter amount you want to deposit: ")
#         if amount.isdigit():
#             amount = int(amount)
#             if amount > 0:
#                 break
#             else:
#                 print("please enter amount greater than 0. ")

#         else:
#             print("please enter a number!")

#     Account_details.append(int(AccountNo))
#     Account_details.append(amount)
#     return Account_details


# Account_details = deposit()

# data = user_details + Account_details

# print(data)


# def login():
#     cred = ""
#     first_name = input("Enter your Firstname: ")
#     cred = cred + " " + first_name
#     last_name = input("Enter your Last_name: ")
#     cred = cred + " " + last_name
#     Account_no = input("Enter your AccountNo: ")
#     cred = cred + " ," + Account_no
#     Password = input("Enter your password: ")
#     cred = cred + " ," + Password

#     return cred


# print(login())

def lambda_handler(event, context):

    path = event["path"]
    Method = event['httpmethod']

    if '/register' in path and Method == 'Post':
        return Createuser(event)

    else:
        log.info("No Matching resource found - 404")

        return Response(404, "Resource Not Found")
