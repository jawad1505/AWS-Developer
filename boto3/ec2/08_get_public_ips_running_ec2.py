import boto3

ec2 = boto3.client('ec2')
reservations = ec2.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")

for reservation in reservations:
    for instance in reservation['Instances']:
        print(instance.get("PublicIpAddress"))

        