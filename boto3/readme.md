Client and Resource are two different abstractions within the boto3 SDK for making AWS service requests. 

Session is largely orthogonal to the concepts of Client and Resource (but is used by both).

Client:

this is the original boto3 API abstraction
provides low-level AWS service access
all AWS service operations are supported by clients
exposes botocore client to the developer
typically maps 1:1 with the AWS service API
snake-cased method names (e.g. [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)  API => [list_buckets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_buckets) method)
generated from AWS service description