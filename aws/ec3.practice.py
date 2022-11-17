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
        id = (ec_client.describe_instances()["Reservations"][0]['Instances'][0]['InstanceId'])
        type = (ec_client.describe_instances()["Reservations"][0]['Instances'][0]['InstanceType'])
        status = (ec_client.describe_instances()["Reservations"][0]['Instances'][0]['State']['Name'])
        name = (ec_client.describe_instances()["Reservations"][0]['Instances'][0]['Tags'][0]['Value'])

        result = name,id,type,status

        id1 = (ec_client.describe_instances()["Reservations"][1]['Instances'][0]['InstanceId'])
        type1 = (ec_client.describe_instances()["Reservations"][1]['Instances'][0]['InstanceType'])
        status1 = (ec_client.describe_instances()["Reservations"][1]['Instances'][0]['State']['Name'])
        name1 = (ec_client.describe_instances()["Reservations"][1]['Instances'][0]['Tags'][0]['Value'])
        
        result1 = name1,id1,type1,status1
        
        #print(ec_client.describe_instances())
    
    except Exception as e:
        print(e)
    return result,result1  

#describe_ec2()

def start_ec2():
    print("starting ec2 instances !!")
        
    try:
        ec_client = boto3.client("ec2")
        start1 = (ec_client.start_instances(
                InstanceIds=[
            'i-0689308e8600f16b7'
    ],
    ))      
    except Exception as e:
        print(e)
    return (start1)  

def start1_ec2():
    print("starting ec2 instances !!")
        
    try:
        ec_client = boto3.client("ec2")
        start2=(ec_client.start_instances(
                InstanceIds=[
            'i-0c4a8087209b927a3'
    ],
    ))      
    except Exception as e:
        print(e)
    return (start2)

def reboot_ec2():
    print("Rebooting Ec2 instances")

    try:
        ec_client = boto3.client('ec2')
        reboot1 = (ec_client.reboot_instances(
                InstanceIds=[
        'i-0689308e8600f16b7'
    ],
    ))  
        
    except Exception as e:
        print(e)   
    return reboot1

def reboot1_ec2():
    print("Rebooting Ec2 instances")

    try:
        ec_client = boto3.client('ec2')
        reboot2 = (ec_client.reboot_instances(
                InstanceIds=[
        'i-0c4a8087209b927a3'
    ],
    ))  
        
    except Exception as e:
        print(e)
    return reboot2

def stop_ec2():
    print("Stop Ec2 instances")
    try:
        ec_client = boto3.client('ec2')
        stop1 = print(ec_client.stop_instances(
                InstanceIds=[
        'i-0689308e8600f16b7'
    ],
        )) 
    except Exception as e:
        print(e)
    return stop1

def stop1_ec2():
    print("Stop Ec2 instances")
    try:
        ec_client = boto3.client('ec2')
        stop2 = print(ec_client.stop_instances(
                InstanceIds=[
        'i-0c4a8087209b927a3'
    ],
        )) 
    except Exception as e:
        print(e)
    return stop2

ids = describe_ec2()
print(ids)

def select(ids):
    d = []
    for x in ids:
        d.append(x)
    one = d[0]
    two = d[1]
    
    message = [" "]
    while message not in [one ,two]: 
        message = input("enter name of the Instances to select Instance:   ")

        if message not in ["one" , "two"]:
            print("please enter a valid input !!")
        else:
            break
    return message 

position = select(ids)

def display(position):
    if "one" in [position]:
        print(ids[0])
        for x in ids[0]:
            if x == 'stopped':
                print(start_ec2())
            elif x == 'running':
                print(reboot_ec2())
                if (reboot_ec2()['ResponseMetadata']['HTTPStatusCode']) == 200:
                    print(stop_ec2())
                else:
                    break
            else:
                print("error")
    
    else: 
        print(ids[1])
        for x in ids[1]:
            if x == 'stopped':
                print(start1_ec2())
            elif x == 'running':
                print (reboot1_ec2())
                if (reboot1_ec2()['ResponseMetadata']['HTTPStatusCode']) == 200:
                    print(stop1_ec2())
                else:
                    break
            else:
                print("error")
    

display(position)