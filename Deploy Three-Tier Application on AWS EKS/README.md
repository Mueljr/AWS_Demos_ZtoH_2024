**This project intends to demonstrate how to deploy a three-tier application on AWS EKS.**

**FRONTEND + BACKEND + DATABASE, ALL DEPLOYED ON AWS EKS AND ACCESSIBLE TO USERS VIA AN INGRESS ALB CONTROLLER'S DNS URL.**

**About App:** Stan's Robot Shop is a sample microservice application designed as a sandbox to test and learn containerized application orchestration and monitoring techniques.

The application deployed has 12 microservices running, and is copped from IBM's Instana.

After initial configurations are done, an **helm chart** is employed for better organization and management.

Helm chart folder as found in this directory contains a chart.yml file, a values.yml file, and an ingress.yml file.

Templates folder for the helm chart contains deployment and service yaml files for about 8 services that would be visible on the front-end (UI).

Also, a few other yaml files for the backend, as well as for the Database tier.
