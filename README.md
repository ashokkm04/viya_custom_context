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