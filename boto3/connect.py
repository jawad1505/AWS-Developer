import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

s3_buckets = list()
# Print out bucket names
for bucket in s3.buckets.all():
    print("s3 bucket: ",bucket.name)
    s3_buckets.append(bucket.name)


print(s3_buckets)
# Upload a new file
data = open('pikachu.jpg', 'rb')
# s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)
s3.Bucket(s3_buckets[0]).put_object(Key='test.jpg', Body=data)