import zipfile
archive = zipfile.ZipFile('function.zip', 'w')
zip.write('index.js', 'path/on/disk/index.js')
.......

client.put_object(Body=archive, Bucket='bucket-name', Key='function.zip')

lambda_Client = boto3.client('lambda', aws_access_key_id=accessKey,
                       aws_secret_access_key=secretKey,region_name=region)
response = lambda_Client.create_function(
            Code={
                'S3Bucket': 'bucket-name',
                'S3Key': 'function.zip', #how can i create or fetch this S3Key
            },
            Description='Process image objects from Amazon S3.',
            FunctionName='function_name',
            Handler='index.handler',
            Publish=True,
            Role='arn:aws:iam::123456789012:role/lambda-role',
            Runtime='nodejs12.x',
        )
