import boto3

# Create IAM client
iam = boto3.client('iam')

# Create user
response = iam.create_user(
    UserName='jawad'
)

print(response)