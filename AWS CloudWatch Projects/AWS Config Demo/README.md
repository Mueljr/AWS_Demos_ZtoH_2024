This project to demonstrate the purpose of compliance of resources as used in organizations, to ensure the list of mandatory things as enlisted by an organization is adhered to on cloud.

**DEMO: An organization has EC2 instance monitoring checked as part of their mandatory policies.**

**Implementation of AWS Config Resource to ensure all EC2 Instances in the organization have their monitoring enabled by verifying if it is in a compliant state or not**

Demo implemented by:

1. Creating two EC2 instances to test for;

2. Integrating a custom Lambda Function that implements JSON and Python Boto3 elements to verify for compliance and non-compliance for the EC2 instances;

3. Creating a custom AWS Config Rule that integrates what the created Lambda Function calls for;

4. AWS CloudWatch metrics and alarms to notify the DevOps engineers if an EC2 instance has gone non-compliant.

**Permissions granted for the Lambda Function includes CloudWatch Full Access, EC2 Full Access, Config_Rule, and CloudTrail Full Access.
Manual monitoring of compliance rules (AWS Config) can also be checked on the "Resource Scope" arm of the Rules.
