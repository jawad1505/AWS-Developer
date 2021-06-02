# AWS TOOLS
  1) Create new user in IAM - > programatic access - > copy key/secret AKIA5GHD6OLXPAJ7AZ7K	oSh5U+veyhFme7c+t0WxL8qwcmOrMtZL3GqovyCn
  2) Download AWS cli 
  3) aws configure
    enter accessKey, Secret, Region
  4) aws sts get-caller-identity
  5) aws ec2 create-key-pair --key-name my-key-pair --query "KeyMaterial" --output text > my-key-pair.pem
     chmod 400 my-key-pair.pem

 6) to see list of EC2
aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId" --output table


----------------
terraform init
terraform plan -out=s1.tfplan
terraform graph
    http://www.jdolivet.byethost13.com/Logiciels/WebGraphviz/?i=1
terraform apply s1.tfplan 

---once done ssh in the new instance

chmod 400 tf_key.pem
ssh -i "tf_key/pem" ec2-user@<new intance dns> 

-----------------


Terraform variables: terraform.tfvards
    String, Boolean, Numberm, List, Set, Map, Object, Tuple 

    terraform plan -var deploy_environment=QA // overwrite variable


-------------
EXPRESSIONS:
terraform console // REPL - Read evaluate print Loop - interactive program
------------

FUNCTIONS:
jawadsalim12@gmail.com

