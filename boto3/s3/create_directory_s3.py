# create directory(ies) in an existing bucket

import boto3
import boto3
s3 = boto3.client('s3')
bucket_name = "js-boto3-demo"

directory_names = [ "test", "best"]
for x in directory_names:
    s3.put_object(Bucket=bucket_name, Key=(x+'/'))