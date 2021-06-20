import boto3
from botocore.exceptions import ClientError

# Create EC2 client
ec2 = boto3.client('ec2')

# Delete security group
try:
    response = ec2.delete_security_group(GroupId='sg-01cf7a9ac45c44b67')
    print('Security Group Deleted')
except ClientError as e:
    print(e)

# import boto3


# ec2 = boto3.client('ec2')
# filters = [
#     {'Name': 'domain', 'Values': ['vpc']}
# ]
# response = ec2.describe_addresses(Filters=filters)
# print(response)