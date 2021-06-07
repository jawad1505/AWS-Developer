Client and Resource are two different abstractions within the boto3 SDK for making AWS service requests. 

Session is largely orthogonal to the concepts of Client and Resource (but is used by both).

## Client:

* this is the original boto3 API abstraction
* provides low-level AWS service access
* all AWS service operations are supported by clients
* exposes botocore client to the developer
* typically maps 1:1 with the AWS service API 
* snake-cased method names (e.g. [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)  API => [list_buckets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_buckets) method)
*  generated from AWS service description
```
import boto3

client = boto3.client('s3')
response = client.list_objects_v2(Bucket='mybucket')
for content in response['Contents']:
    obj_dict = client.get_object(Bucket='mybucket', Key=content['Key'])
    print(content['Key'], obj_dict['LastModified'])
```
> Note: this client-level code is limited to listing at most 1000 objects. You would have to use a paginator, or implement your own loop, calling list_objects_v2() repeatedly with a continuation marker if there were more than 1000 objects.

* default session - list buckets
```
import boto3 
s3 = boto3.client('s3')

def list_bucket_contents(bucket_name):
   for object in s3.list_objects_v2(Bucket=bucket_name) :
      print(object.key)

list_bucket_contents('Mybucket') 
```

* list objects from a bucket in different regions,
```
import boto3 
backup_s3 = my_west_session.client('s3',region_name = 'us-west-2')
video_s3 = my_east_session.client('s3',region_name = 'us-east-1')

# you must pass boto3.Session.client and the bucket name 
def list_bucket_contents(s3session, bucket_name):
   response = s3session.list_objects_v2(Bucket=bucket_name)
   if 'Contents' in response:
     for obj in response['Contents']:
        print(obj['key'])

list_bucket_contents(backup_s3, 'backupbucket')
list_bucket_contents(video_s3 , 'videobucket') 
```

## Resources


* this is the newer boto3 API abstraction
* provides high-level, object-oriented API
* does not provide 100% API coverage of AWS services
* uses identifiers and attributes
* has actions (operations on resources)
* exposes subresources and collections of AWS resources
* generated from resource description

Here's the equivalent example using resource-level access to an S3 bucket's objects (all):

```
import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('mybucket')
for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)
```
Resources + Session
```
import boto3 
my_west_session = boto3.Session(region_name = 'us-west-2')
my_east_session = boto3.Session(region_name = 'us-east-1')
backup_s3 = my_west_session.resource("s3")
video_s3 = my_east_session.resource("s3")
backup_bucket = backup_s3.Bucket('backupbucket') 
video_bucket = video_s3.Bucket('videobucket')

# just pass the instantiated bucket object
def list_bucket_contents(bucket):
   for object in bucket.objects.all():
      print(object.key)

list_bucket_contents(backup_bucket)
list_bucket_contents(video_bucket)
```
## Session:
is where to initiate the connectivity to AWS services. E.g. following is default session that uses the default credential profile(e.g. ~/.aws/credentials, or assume your EC2 using IAM instance profile )

* stores configuration information (primarily credentials and selected region)
* allows you to create service clients and resources
* boto3 creates a default session for you when needed

```
# custom resource session must use boto3.Session to do the override
my_west_session = boto3.Session(region_name = 'us-west-2')
my_east_session = boto3.Session(region_name = 'us-east-1')
backup_s3 = my_west_session.resource('s3')
video_s3 = my_east_session.resource('s3')

# you have two choices of create custom client session. 
backup_s3c = my_west_session.client('s3')
video_s3c = boto3.client("s3", region_name = 'us-east-1')
```
# Reference / Quick Start
* [AWS: introduction boto3 - Youtube](https://www.youtube.com/watch?v=Cb2czfCV4Dg)
* [aws-modern-application-workshop](https://github.com/aws-samples/aws-modern-application-workshop/tree/python)

* [boto3](https://github.com/boto/boto3)

* [boto3 quick start](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

* [AWS SDK boto3](https://aws.amazon.com/sdk-for-python/)

* [boto 3 components](https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session)

* [AWS DEMO: Build a Modern Web Application](https://aws.amazon.com/getting-started/hands-on/build-modern-app-fargate-lambda-dynamodb-python/)