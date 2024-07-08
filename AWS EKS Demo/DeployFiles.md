**STAGE 5**

**DEPLOY POD, DEPLOYMENT, SERVICE, AND INGRESS YAML FILES FROM YOUR TERMINAL**

All of these files are required for the application in view to be deployed successfully into the cluster.
While Pod.yml files roll out a single instance of a running process in the cluster, deployment.yml files manages a set of identical pods with declarative updates.
Service.yml files on the other hand describes policies and permission wherein a pod can be accessed.
Ingress.yml files act as a resource that defines the rules for routing external traffic from users, to the internal services in your app.

In this case, all configurations are described in one single yaml file as found on the official EKS repository on GitHub.
If you were to do it personally, you could write everything down and save as one yaml source code file.
This will aid in a seamless implementation of all four yaml file configuration via just a command line

Command: _kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.5.4/docs/examples/2048/2048_full.yaml_

If stored in your personal repository or any other one: _kubectl apply -f _yamlfile link__
