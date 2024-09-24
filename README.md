Lambda Function
Receive and Parse the Incoming Event:

The Lambda function is designed to handle incoming events that include a JWT token, user ID, and project name.
Initialize the AWS Secrets Manager Client:

The function begins by creating a session and client to interact with AWS Secrets Manager.
Retrieve Secret from Secrets Manager:

Using the secret's ARN, the function retrieves the secret AWS key pairs associated with the specified project from Secrets Manager.
Process Response:

After retrieving the AWS keys, the response is formatted as response.json.
ConfigMap Logic
The ConfigMap is structured to perform the following steps:

1. Lambda Invocation:

From the sidecar container, the Lambda function is invoked using the username, JWT token, and project name.


2. Process Response JSON:

The response.json from the Lambda invocation is processed. The AWS credentials are then written to a credentials file located in the /etc/.aws shared mount volume with compute. This setup enables the corresponding project user to access the S3 bucket.
Policies and Roles
Group Policies:

Group policies for each project can be created using a standard template policy (project_group_policy).
Lambda Execution Role Policy:

A specific policy (lambda_execution_role_permission) allows the Lambda function to execute and access secrets, along with its associated assume role policy.
Service Account Role Policy:

This policy (service_account_role) provides the role necessary to invoke the Lambda function from the EKS cluster, which is enabled with IRSA/OIDC. The associated assume role policy is also defined.




This project contains the implementation code for setting up SAS Viya custom context. Below are the instructions for creating the necessary AWS resources using AWS CLI commands.


Prerequisites
Ensure you have the following:

AWS CLI installed and configured with appropriate access rights.
Necessary IAM permissions to create resources.

## Steps to Create AWS Resources

### 1. S3 Bucket
Create an S3 bucket to store Viya-related data.

```bash
aws s3 mb s3://<your-bucket-name>

###2. IAM Role
Create an IAM role with permissions for Viya services.

aws iam create-role --role-name <your-role-name> \
  --assume-role-policy-document file://trust-policy.json

aws iam attach-role-policy --role-name <your-role-name> \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
aws iam attach-role-policy --role-name <your-role-name> \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess

3. Lambda Function
Create a Lambda function to handle custom operations.
zip function.zip index.js
aws lambda create-function --function-name <your-function-name> \
  --zip-file fileb://function.zip \
  --handler index.handler \
  --runtime nodejs14.x \
  --role arn:aws:iam::<your-account-id>:role/<your-role-name>



