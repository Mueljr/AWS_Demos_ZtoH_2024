**STAGE 6**

**Add an Ingress Controller**

Essentially, for your ingress resource to function as described on the ingress.yml file, there is the need for an ingress controller.
It helps implement the rules stated out in the ingress resource, and fulfils the ingress. It is basically a "router" from the outside world to the ingress resource.

How is this implemented? This is implemented by configuring a load balancer or proxy server.

In this case, since we're dealing with AWS EKS, AWS has its own default & managed load balancer - AWS Load Balancer or Application Load Balancer (ALB).

This ingress controller when created will create an ALB, and also, configure it automatically.

**STEPS**
1. Configure IAM OIDC Provider

   Command: _eksctl utils associate-iam-oidc-provider --cluster $cluster_name --approve_

3. Download the official IAM Policy for ALB Ingress Controller

    Command: _curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/install/iam_policy.json_

4. Create IAM Policy to grant permissions

   Command: _aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json_

6. Create IAM Role to enable communication between the EKS Service and your ALB Controller

   Command: _eksctl create iamserviceaccount \
  --cluster=<your-cluster-name> \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name AmazonEKSLoadBalancerControllerRole \
  --attach-policy-arn=arn:aws:iam::<your-aws-account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve_

8. Finally Deploy the ALB Controller via Helm Chart
   a. Add Helm Repository - _helm repo add eks https://aws.github.io/eks-charts_
   
   b. Update Helm Repository - _helm repo update eks_
   
   c. Install Helm Chart - _helm install aws-load-balancer-controller eks/aws-load-balancer-controller \            
  -n kube-system \
  --set clusterName=<your-cluster-name> \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set region=<region> \
  --set vpcId=<your-vpc-id>_
