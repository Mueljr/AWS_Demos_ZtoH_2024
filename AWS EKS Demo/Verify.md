**FINAL STAGE**

**VERIFY THAT 2 REPLICAS OF YOUR DEPLOYMENT ARE RUNNING**

You should be able to view the address for users to access the game application. This way, your app is secured in the private subnet of the VPC within the cluster, and users can still access it, thanks to the ingress controller.
Command: _kubectl get deploy -n kube-system_

Make sure your Load Balancer as listed on your EC2 Instances feature is on an active state before launching the address to access the application.

Address should be launched with the http:// or https:// prefix on your preferred browser.

**If encountering any errors on the go, probably due to intermittent network issues or whatever the case may be, you could for to the Cloud Formation Templates (CFT) on your AWS Console and delete the stack related to this deployment, after which you can start again.
