**Three-tier application is deployed on AWS EKS using helm charts.**

Folder contains a chart.yml file, a values.yml file, and an ingress.yml file.

Templates folder for the helm chart contains deployment and service yaml files for about 8 services that would be visible on the front-end (UI).

Also, a few other yaml files for the backend, as well as for the Database tier.

**STEPS IN FINAL DEPLOYMENT**

1. Create Namespace

$ kubectl create ns <namespace>

2. Install Helm

$ helm install <helmreleasename> --namespace <namespace> .

3. Verify Pods are running

kubectl get pods -n <namespace>

4. Apply ingress.yml configuration

kubectl apply -f ingress.yaml

5. Finally wait for the load balancer to be on active state on the UI, and launch Ingress controller's DNS on browser to access Stan Robot Shop's application.
