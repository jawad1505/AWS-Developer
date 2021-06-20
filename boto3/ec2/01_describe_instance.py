# import boto3

# ec2 = boto3.client('ec2')
# # response = ec2.describe_instances()
# response = ec2.describe_instances(

# )
# print(response['Reservations'])

import sys
import boto3


ec2 = boto3.client('ec2')
# if sys.argv[1] == 'ON':
response = ec2.unmonitor_instances(InstanceIds=['i-009a95d9177736a94'])
# else:
#     response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)