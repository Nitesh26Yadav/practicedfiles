import boto3

s3 = boto3.client('s3',
    aws_access_key_id = "AKIATABGVN5PEF4BS5PR",
    aws_secret_access_key = "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")

def create_ec2():
    print('Creating EC2 instances')
    try:
        ec_client = boto3.client('ec2')
        ec_client.run_instances(
            ImageId = 'ami-08df646e18b182346',
            MinCount = 1,
            MaxCount = 1,
            InstanceType = 't2.micro',
            KeyName = 'EC2'
        )
    except Exception as e :
        print(e)

    
def describe_ec2():
    print("describing EC2 Instances")
    try:
        ec_client = boto3.client('ec2')
        #id = (ec_client.describe_instances()["Reservations"][0]['Instances'][0]['InstanceId'])
        id =print(ec_client.describe_instances())
    except Exception as e:
        print(e)
    return id

def stop_ec2():
    print("Stop Ec2 instances")
    try:
        ec_client = boto3.client('ec2')
        abc = print(ec_client.stop_instances(
                InstanceIds=[
        'i-0689308e8600f16b7'
    ],
        )) 
    except Exception as e:
        print(e)
    return abc

def describe_ec2(var):
    print("describing stop Ec2 instances ")
    try:
        ec_client = boto3.client('ec2')
        var = (ec_client.describe_instances()['Reservations'][0]['Instances'][0]['State']['Name'])
        print(var)
    except Exception as e:
        print(e)
    return var

def reboot_ec2():
    print("Rebooting Ec2 instances")

    try:
        ec_client = boto3.client('ec2')
        print(ec_client.reboot_instances(
                InstanceIds=[
        'i-0689308e8600f16b7'
    ],
    ))  
        
    except Exception as e:
        print(e)

def start_ec2():
    print("starting ec2 instances !!")
        
    try:
        ec_client = boto3.client("ec2")
        print(ec_client.start_instances(
                InstanceIds=[
            'i-0689308e8600f16b7'
    ],
    ))      
    except Exception as e:
        print(e)
    return ("Ec2 instances is successfull! and Running!")

#create_ec2()
#describe_ec2()

var = stop_ec2()


if describe_ec2(var)  not in "stopped":
    print("Alert :" " It is in stopping state")
    print("Message :" " Wait for 1 minute and Run the code")

reboot_ec2()

if reboot_ec2 != 200:
    print("Rebooting instances failed !!")
    print(start_ec2())
else:
    print("Rebooting instances is success !!")





