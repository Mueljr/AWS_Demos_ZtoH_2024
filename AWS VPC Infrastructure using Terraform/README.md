**AWS VPC INFRASTRUCTURE USING TERRAFORM**

This project demonstrates how an application (an html source code in this case) can be deployed into a VPC, having two subnets (both public), with an S3 bucket to store the objects required.

In this case:

**VPC** - to enable better security for the infrastructure utilizing security tools such as Internet Gateway, Security Groups.

**Subnets** - both public subnets to aid in better availability, as two availability zones are used; one per subnet.

**Route table** - implemented to both subnets, with a route table association to define packets routed to each subnet.

**Load Balancer** - implemented to balance the amount of traffic coming into the subnets, by switching availability between two zones, hence, better scalability and availability. Load balancer target group also implemented, with a target group attachment and listener. Application Load Balancer is implemented in this case.

**EC2 Instances** - one instance per subnet launched, with an availability zone each.

**S3 Bucket** - implemented to store objects required.

All of these resources are implemented using Terraform for faster automation purposes.
AWS Account is authenticated on CLI, and a new directory is created, with Visual Studio Code used to enter the necessary configurations and launch the commands.

**provider.tf file contains the required syntaxes and configuration for terraform to communicate with the AWS provider**

**main.tf file contains all the necessary configurations for this set-up from creating a vpc to the entire set-up.**
Terraform AWS Documentation + the UI referred to for structuring configurations on the CLI.

**variable.tf file created to store the CIDR block variable**

**userdata1.sh and userdata2.sh files as specified for each instance, contains a simple html source file with a fictional instance ID stored in a local IP address. It is encoded as base64 in the Terraform config, and switches between both html pages when launched on the browser due to the load balancer at work, causing maximum availability.**
