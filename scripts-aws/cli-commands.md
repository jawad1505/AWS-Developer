aws --version

# key, secret, region,
aws configure

# list users
aws iam list-users


aws lambda list-functions

aws lambda invoke --function-name demopythonlam --cli-binary-format raw-in-base64-out --payload '{"key1": "value1", "key2": "value2", "key3": "value3" }' --region us-east-2 response.json

aws lambda invoke --function-name demopythonlam --cli-binary-format raw-in-base64-out --payload '{"key1": "rajab", "key2": "value2", "key3": "value3" }' --invocation-type Event --region us-east-2 response.json


# s3
Commands:
```
cp
ls
mb
mv
presign
rb
rm
sync
website
```
Examples:
```
aws s3 ls

aws s3 ls s3://bucketname

aws s3 cp s3://demo-js15-s3-bucket/pikachu.jpg pikachu.jpg


aws s3 mb s3://mybucket

aws s3 rb s3://mybucket

ami-0d8d0b22f8144dc66

aws ec2 run-instances --image-id ami-0d8d0b22f8144dc66 --instance-type t2.micro --dry-run
```

* S3 access logs - Serer Access loggin - logs in another s3

S3 Replication:
* CRR - use case: compliance, lower latency access,replication accross accounts
* SRR - use case: log aggregation, live replication btw production and test accounts
* No chaining 

* S3 -> Management -> Replication Rules
    Source: all or limit
    destination: s3 buck in same or diff region

* S3 -> Pre signed URLs


docker tag js-http-image:latest public.ecr.aws/y9u1f1a4/js-demo-ecr:latest


docker push public.ecr.aws/y9u1f1a4/js-httpd-image:latest


aws lambda add-permission   --function-name "arn:aws:lambda:us-east-1:805942555403:function:lambda-api-gatway-:DEV"   --source-arn "arn:aws:execute-api:us-east-1:805942555403:wwr1l4f8cc/*/GET/stagevariables"   --principal apigateway.amazonaws.com   --statement-id d238be49-2218-425a-8e5f-96b1d69fdf85   --action lambda:InvokeFunction --region us-east-1
RESULT: 
{
    "Statement": "{\"Sid\":\"d238be49-2218-425a-8e5f-96b1d69fdf85\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"apigateway.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:us-east-1:805942555403:function:lambda-api-gatway-:DEV\",\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:execute-api:us-east-1:805942555403:wwr1l4f8cc/*/GET/stagevariables\"}}}"
}


aws lambda add-permission   --function-name "arn:aws:lambda:us-east-1:805942555403:function:lambda-api-gatway-:TEST"   --source-arn "arn:aws:execute-api:us-east-1:805942555403:wwr1l4f8cc/*/GET/stagevariables"   --principal apigateway.amazonaws.com   --statement-id d238be49-2218-425a-8e5f-96b1d69fdf85   --action lambda:InvokeFunction --region us-east-1

aws lambda add-permission   --function-name "arn:aws:lambda:us-east-1:805942555403:function:lambda-api-gatway-:PROD"   --source-arn "arn:aws:execute-api:us-east-1:805942555403:wwr1l4f8cc/*/GET/stagevariables"   --principal apigateway.amazonaws.com   --statement-id d238be49-2218-425a-8e5f-96b1d69fdf85   --action lambda:InvokeFunction --region us-east-1



SAM 
  GNU nano 5.2                                                             commands.sh                                                              Modified
