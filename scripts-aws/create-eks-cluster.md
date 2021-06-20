eksctl create cluster \
--name js-cluster \
--region us-east-2 \
--with-oidc \
--ssh-access \
--ssh-public-key awseks \
--node-type t2.micro \
--nodes-max 9 \
--nodes-min 3 \
--managed

eksctl create cluster \
    -n $NAME \
    -r $AWS_DEFAULT_REGION \
    --kubeconfig cluster/kubecfg-eks \
    --node-type t2.micro \
    --nodes-max 9 \
    --nodes-min 3 \
    --asg-access \
    --managed