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
        
        id =ec_client.describe_instances()
        x = []
        for ins in id['Reservations']:
            for ids in ins['Instances']:
                for name in ids['Tags']:
                    data = (name['Value'],ids['InstanceId'],ids['InstanceType'],ids['State']['Name'])
                    x.append(data)
            
        return(x)
    except Exception as e:
        print(e)
    return x

lis = describe_ec2()
print(lis)

def select(lis):
    message = [""]
    message = input("enter name of the Instances to select Instance:   ")
    print(message)

    for each in lis:
        if message in each :
            ri =  each
            break
        elif message not in each:
            print('please enter valid input')
        

    return(ri) 


def start_ec2(r):
    print("starting ec2 instances !!")
    
    try:
        ec_client = boto3.client("ec2")
        print(ec_client.start_instances(

                    InstanceIds=[
                    r[1]
    ],                  
    ))      

    except Exception as e:
        print(e)

def reboot_ec2(r):
    print("Rebooting Ec2 instances")

    try:
        ec_client = boto3.client('ec2')

        print(ec_client.reboot_instances(
                InstanceIds=[
                    r[1]
    ],
    ))  

    except Exception as e:
        print(e)   


def stop_ec2(r):
    print("Stop Ec2 instances")

    try:
        ec_client = boto3.client('ec2')    
    
        print(ec_client.stop_instances(
        InstanceIds=[
                    r[1]
                       
    ],
    )) 

    except Exception as e:
        print(e)

r = select(lis)
print(r)


if 'stopped' in r:
    print(start_ec2(r))

elif 'running' in r:
    choice = ['8748748']
    while choice not in ['reboot','stop']:
        choice= input("select the function you want to run reboot,stop:  ")
    

        if  choice not in ['reboot','stop']:
            print("please enter valid input !!")
        
        else:   
            break
    print (choice)

    if choice =='reboot':
        print(reboot_ec2(r))
    elif choice == 'stop':
        print(stop_ec2(r))
