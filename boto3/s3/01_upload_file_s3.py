import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

bucket_name = 's3-boto-js'

# Upload a new file
data = open('pikachu.jpg', 'rb')
s3.Bucket(bucket_name).put_object(Key='pikachu.jpg', Body=data)