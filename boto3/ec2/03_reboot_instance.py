import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=['i-009a95d9177736a94'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances.")
        raise

try:
    response = ec2.reboot_instances(InstanceIds=['i-009a95d9177736a94'], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)