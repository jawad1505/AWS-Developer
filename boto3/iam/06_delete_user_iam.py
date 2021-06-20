import boto3

# Create IAM client
iam = boto3.client('iam')

# Delete a user
res = iam.delete_user(
    UserName='saleem'
)

print(res)