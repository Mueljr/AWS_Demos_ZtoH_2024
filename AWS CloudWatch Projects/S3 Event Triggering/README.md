![s3-event-triggering](https://github.com/user-attachments/assets/4064c2bb-f033-4ac7-b993-4bab7fc37e29)

**Project: Demo on AWS S3 Event Triggering**

This project demonstrates how to set up an event-driven architecture using AWS services. When a media file is uploaded to an S3 bucket, it triggers a Lambda function that processes the event and sends a notification through SNS. This setup involves configuring IAM roles, S3, Lambda, and SNS using a shell script with the AWS CLI.

**Using Shell Script for AWS Resource Management:**

Using a shell script for managing AWS resources is faster and more efficient compared to manually configuring resources via the AWS Management Console. The script ensures consistency and repeatability, reducing the chances of human error. Alternatives to using AWS CLI shell scripts include Infrastructure as Code (IaC) tools such as Terraform and AWS CloudFormation, which provide more robust and scalable solutions for managing AWS infrastructure.

**Requirements:**
- AWS CLI and `jq` installed.
- An object (file) to be stored in the S3 bucket.
- Execute project with shell script.

**Lambda Function Python Code Review:**

1. **Initialization:**
   - Retrieves the AWS account ID and sets the AWS region and resource names.

2. **IAM Role Creation:**
   - Creates an IAM role with permissions to be assumed by Lambda, S3, and SNS.
   - Attaches policies for Lambda and SNS full access.

3. **S3 Bucket Creation:**
   - Creates an S3 bucket and uploads a sample file to it.

4. **Lambda Function Creation:**
   - Zips the Lambda function code and creates the Lambda function using the specified role.

_When running the script, ensure it's executed in a directory containing your Lambda files (`lambda_function.py` and `requirements.txt`). The script will create a temporary directory, copy your Lambda files into it, install dependencies from `requirements.txt`, zip the directory's contents, and then create the Lambda function on AWS using the AWS CLI. This process is necessary because AWS Lambda requires the function code to be uploaded as a zip file when using the AWS CLI._

   - Adds permissions for S3 to invoke the Lambda function.

5. **S3 Event Trigger Configuration:**
   - Configures S3 to trigger the Lambda function on object creation events.

6. **SNS Topic Creation:**
   - Creates an SNS topic and subscribes an email endpoint to it.
   - Publishes a test message to the SNS topic.

**Running the Script and Uploading to GitHub**

**Local Execution:**
1. Ensure all Lambda function files are stored locally in a directory.
2. Navigate to the directory in your terminal.
3. Run the shell script to set up the resources.

**Uploading to GitHub:**
1. Once the resources are set up, you can upload the script and related files to GitHub.
2. Use a version control system like Git to push your local directory to a GitHub repository.
3. This allows you to maintain version control and collaborate with others.
