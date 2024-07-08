**STAGE 2**

**Create Cluster from your Terminal**

In most cases, in the production environment, you would be required to create clusters in bulk, and it would be tedious and stressful to create one after the other on the UI.

So, no matter the amount of clusters proposed to be created, it is good practice to create EKS clusters on the CLI with Fargate as the compute engine option as opposed to EC2 Instances.

Command: _eksctl create cluster --name demo-cluster --region us-east-1 --fargate_

Specify the name of the cluster to be created, as well as the region your app is based.

The cluster will create both a private and public subnet, as well as everything needed at a default level; less strenuous compared to when done on the UI.
