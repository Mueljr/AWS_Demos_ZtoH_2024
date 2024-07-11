**File intends to roll out necessary configurations before going on to deploy the helm chart.**

**STAGE 1**

(A) Install Kubectl and eksctl on your terminal

"kubectl" is a command line tool that grants you access to work with and play around with Kubernetes clusters.

"eksctl" is also a command line tool that helps you automate and implement EKS-related tasks from your CLI.

(B) Install AWS CLI on your terminal

AWS CLI is a command line tool that is pertinent for you working with all AWS services from the comfort of your CLI.

(C) Authenticate your AWS Account on your terminal

Command: _aws configure_

Put in all your AWS account details to link your accout to your terminal to automate and effect changes from that environment.

**For steps A & B, the official AWS documentations can be looked into to access the right commands as your device demands.

**STAGE 2**

**INSTALL EKS CLUSTER USING FARGATE**

Command: _eksctl create cluster --name demo-cluster-three-tier-1 --region us-east-1_


**STAGE 3**

**CONFIGURE IAM OIDC PROVIDER**

_export cluster_name=<CLUSTER-NAME>_

_oidc_id=$(aws eks describe-cluster --name $cluster_name --query "cluster.identity.oidc.issuer" --output text | cut -d '/' -f 5)_

_eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve_

**STAGE 4**

**CONFIGURE ALB INGRESS CONTROLLER**

Essentially, for your ingress resource to function as described on the ingress.yml file, there is the need for an ingress controller. It helps implement the rules stated out in the ingress resource, and fulfils the ingress. It is basically a "router" from the outside world to the ingress resource.

How is this implemented? This is implemented by configuring a load balancer or proxy server.

In this case, since we're dealing with AWS EKS, AWS has its own default & managed load balancer - AWS Load Balancer or Application Load Balancer (ALB).

This ingress controller when created will create an ALB, and also, configure it automatically.

**STEPS**

1. Configure IAM OIDC Provider

Command: eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve

2. Download the official IAM Policy for ALB Ingress Controller

Command: curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/install/iam_policy.json

3. Create IAM Policy to grant permissions

Command: aws iam create-policy
--policy-name AWSLoadBalancerControllerIAMPolicy
--policy-document file://iam_policy.json

4. Create IAM Role to enable communication between the EKS Service and your ALB Controller.

Command: eksctl create iamserviceaccount
--cluster=
--namespace=kube-system
--name=aws-load-balancer-controller
--role-name AmazonEKSLoadBalancerControllerRole
--attach-policy-arn=arn:aws:iam:::policy/AWSLoadBalancerControllerIAMPolicy
--approve

5. Finally, deploy the ALB Controller via Helm Chart
   
a. Add Helm Repository - helm repo add eks https://aws.github.io/eks-charts

b. Update Helm Repository - helm repo update eks

c. Install Helm Chart - helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
-n kube-system
--set clusterName=
--set serviceAccount.create=false
--set serviceAccount.name=aws-load-balancer-controller
--set region=
--set vpcId=

**STAGE 5**

**EBS CSI PLUGIN CONFIGURATION**

The Amazon EBS CSI plugin needs IAM permissions to call AWS APIs on your behalf. Create an IAM role and attach a policy. You can use an AWS-managed policy or create your own custom policy. To create an IAM role and attach the AWS-managed policy, run the following command, replacing my-cluster with your cluster name. This command deploys a CloudFormation stack to create the IAM role and attach the policy.

Essentially, for the Database tier used by organizations as part of a three-tier application, 99% of the time, Redis is created as a stateful set. Once Redis is employed for the in-memory data store such as the 'Cart' feature in the application, they create Persistent Volumes (PVs), also known as the EBS.

Once EKS is attached to an EBI CSI plugin, it creates a Persistent Volume Claim (PVC), which in turn creates an EBS volume that attaches itself to the stateful set. This allows for proper communication between volumes (EBS) as in the database, and the AWS EKS resource.

**STEPS**

1. Create IAM Role and Policy

eksctl create iamserviceaccount \
    --name ebs-csi-controller-sa \
    --namespace kube-system \
    --cluster <YOUR-CLUSTER-NAME> \
    --role-name AmazonEKS_EBS_CSI_DriverRole \
    --role-only \
    --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
    --approve

2. Create add-on

eksctl create addon --name aws-ebs-csi-driver --cluster <YOUR-CLUSTER-NAME> --service-account-role-arn arn:aws:iam::<AWS-ACCOUNT-ID>:role/AmazonEKS_EBS_CSI_DriverRole --force
