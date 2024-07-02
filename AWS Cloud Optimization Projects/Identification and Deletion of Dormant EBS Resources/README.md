Use Case: EBS Backup Volume Resources (Snapshots).

This AWS Cloud Cost Optimization project focuses on creating a Lambda function that fetches all EBS snapshots, and filters the dormant and active snapshots.
Dormant EBS snapshots in this case have their associated volumes not linked with any active EC2 instance. Active EBS snapshots in this case have their associated volumes linked with an active EC2 instance.
Dormant or Stale EBS snapshots if found are deleted, thus improving efficiency of resources, and aiding in the optimization of EBS storage costs.
