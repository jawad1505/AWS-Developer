"""
GOAL: create lambda function, s3 bucket, permissions, roles, triggers 

1) Create Execution Role
2) Crate Lambda Function - Latest
3) Create Lambda Version - TEST
4) update lambda handler
5) Crate Lamba Version   - PROD
6) Create Bucket A       - TEST
7) Create Bucket B       - PROD
8) Create Bucket Permission to invoke Lambda       - TEST
9) Create Bucket Permission to invoke Lambda       - PROD
10) Create Bucket Trigger to invoke Lambda       - TEST
10) Create Bucket Trigger to invoke Lambda       - PROD
"""


import logging
import json, boto3, yaml
from botocore.exceptions import ClientError

config = yaml.load("""
                   role: BasicLambdaRole
                   name: HelloWorld
                   zip: HelloWorld.zip
                   path: ./hello.py
                   handler: hello.handler
                   """)


def setup_roles():
    """ Sets up AWS IAM roles for executing this lambda function. """


    basic_role = """
    Version: '2012-10-17'
    Statement:
        - Effect: Allow
          Principal: 
            Service: lambda.amazonaws.com
          Action: sts:AssumeRole
    """

    iam = boto3.client('iam')
    role = iam.get_role(RoleName=config['role'])
    
    if not role:
        # lambda.awazonaws.com can assume this role. 
        iam.create_role(RoleName=config['role'], 
            AssumeRolePolicyDocument=json.dumps(yaml.load(basic_role)))

        # This role has the AWSLambdaBasicExecutionRole managed policy.
        iam.attach_role_policy(RoleName=config['role'], 
            PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole')
        print("created role: ",config['role'])
    else:
        print("role exists: ",config['role'])

# create lambda
def create_lambda():
    """ Creates and uploads the lambda function. """

    lam = boto3.client('lambda')
    iam = boto3.client('iam')

    # Creates a zip file containing our handler code.
    import zipfile
    with zipfile.ZipFile(config['zip'], 'w') as z:
        z.write(config['path'])

    # Loads the zip file as binary code. 
    with open(config['zip'], 'rb') as f: 
        code = f.read()

    role = iam.get_role(RoleName=config['role'])
    print(role)
    return lam.create_function(
        FunctionName=config['name'],
        Runtime='python3.6',
        Role=role['Role']['Arn'],
        Handler=config['handler'],
        Code={'ZipFile':code})

def update_function():
    """ Updates the function. """

    lam = boto3.client('lambda')

    # Creates a zip file containing our handler code.
    import zipfile
    with zipfile.ZipFile(config['zip'], 'w') as z:
        z.write(config['path'])

    # Loads the zip file as binary code. 
    with open(config['zip'], 'rb') as f: 
        code = f.read()

    return lam.update_function_code(
        FunctionName=config['name'],
        ZipFile=code)


def create_lambda_version():
    lam = boto3.client('lambda')
    sha_b = ""
    response = lam.publish_version(
        CodeSha256=r"d0xUQKgJ3+5vw3F2/xuptTTvdxII/+XEmydCQRwOcyk=",
        Description='my version',
        FunctionName=config['name'],
    )

    print(response)

# create bucket
def create_bucket(bucket_name, region=None):
    
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def create_s3_trigger_permissions(lambda_name, s3_arn):
    lam = boto3.client('lambda')
    response = lam.add_permission(
        FunctionName=lambda_name,
        StatementId='1',
        Action='lambda:InvokeFunction',
        Principal='s3.amazonaws.com',
        SourceArn=s3_arn,
        SourceAccount='805942555403'
    )
# create event
def create_s3_trigger(lambda_arn, bucket_name):
    s3 = boto3.resource('s3')
    # bucket_name = bucket_name
    
    bucket_notification = s3.BucketNotification(bucket_name)
    response = bucket_notification.put(
        NotificationConfiguration={'LambdaFunctionConfigurations': [
            {
                'LambdaFunctionArn': lambda_arn,
                'Events': [
                    's3:ObjectCreated:*'
                ],

            },
        ]})
    return response

def invoke_function(first, last):
    """ Invokes the function. """

    lam = boto3.client('lambda')
    resp = lam.invoke(
        FunctionName=config['name'],
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload=json.dumps({'first_name': first, 'last_name': last}))

    print(resp['Payload'].read())
    return resp
# main

# setup_roles()

# res = create_lambda()
# print(res)
# print("="*20)

# resa  = create_lambda_version('Q2KZfyH8tPh7ZWiQgq79XpECuZG/cuA9IRc1xWtM0FE=')
# print("="*20)
# print(resa)

# update_res = update_function()
# print(update_res)

# resb  = create_lambda_version()

# print("="*20)
# print(resb)

# create_bucket('lambda-bucket-js-a','us-east-2')
# create_bucket('lambda-bucket-js-b','us-east-2')

# res = create_s3_trigger_permissions('arn:aws:lambda:us-east-2:805942555403:function:HelloWorld:2', 'arn:aws:s3:::lambda-bucket-js-b')
# print("="*20)
# print(res)

# res = create_s3_trigger('arn:aws:lambda:us-east-2:805942555403:function:HelloWorld:2','lambda-bucket-js-b')
# print("="*20)
# print(res)

# res = create_s3_trigger_permissions('arn:aws:lambda:us-east-2:805942555403:function:HelloWorld:1', 'arn:aws:s3:::lambda-bucket-a')
# print("="*20)
# print(res)

# res = create_s3_trigger('arn:aws:lambda:us-east-2:805942555403:function:HelloWorld:1','lambda-bucket-a')
# print("="*20)
# print(res)


