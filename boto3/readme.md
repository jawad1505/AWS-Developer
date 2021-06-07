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

## Session:

* stores configuration information (primarily credentials and selected region)
* allows you to create service clients and resources
* boto3 creates a default session for you when needed

# Reference / Quick Start

* [aws-modern-application-workshop](https://github.com/aws-samples/aws-modern-application-workshop/tree/python)

* [boto3](https://github.com/boto/boto3)

* [boto3 quick start](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

* [AWS SDK boto3](https://aws.amazon.com/sdk-for-python/)

* [boto 3 components](https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session)