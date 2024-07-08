**STAGE 4**

**Create Fargate Profile for your Cluster from your Terminal**

_Fargate_ is an alternative compute engine to EC2 Instances. They're a serverless compute engine, contrary to EC2's server-based compute engines
With Fargates, you don't have to manage the underlying infrastructure as they fully automate deployment, having better seamless features compared to EC2.
It is the default compute engine option when creating containers on ECS.

Command: _eksctl create fargateprofile \
    --cluster demo-cluster \
    --region us-east-1 \
    --name alb-sample-app \
    --namespace game-2048_

Edit the necessaries, and give it a unique namespace that is consistent throughout.
