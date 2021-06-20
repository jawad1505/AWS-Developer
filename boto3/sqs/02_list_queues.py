import boto3

# Create SQS client
sqs = boto3.client('sqs')

# List SQS queues
sdf
response = sqs.list_queues()

print(response['QueueUrls'])