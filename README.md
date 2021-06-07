# AWS-Developer

# SSH EC2
```
ssh -i <key.pem> ec2-user@<PublicIP>
ssh -i awsdev-keypair.pem ec2-user@18.117.147.214
```
Dont configure aws on EC2, use roles

# get meta-data from ec2
http://169.254.169.254/latest/meta-data/