import boto3

## USING RESOURCE

# # Get the service resource
# sqs = boto3.resource('sqs')

# # Create the queue. This returns an SQS.Queue instance
# queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# # You can now access identifiers and attributes
# print(queue.url)
# print(queue.attributes.get('DelaySeconds'))

## USING CLIENT
client = boto3.client('sqs')

response = client.list_queues(QueueNamePrefix='string',MaxResults=123)

print(response)