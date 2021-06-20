import boto3
import json
from datetime import datetime

# Create IAM client
iam = boto3.client('iam')

response = iam.list_policies()

for key in response['Policies']:
    print (key['PolicyName'])



# print(response['Policies'][0].get('PolicyId'))


# print(iam.list_policies().get('PolicyId'))

