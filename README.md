Lambda function (Receive and Parse the Incoming Event): The Lambda function receives an event that includes a JWT token, user ID, and project name.

Initialize the AWS Secrets Manager Client: Create a session and client to interact with AWS Secrets Manager

Retrieve Secret from Secrets Manager: The function retrieves the secret AWS key pairs for specific project from Secrets Manager using the secret's ARN.

Once the AWS keys were retrived as response.json from Lambda function 

Logic in the ConfigMap: Has 2 steps 
Lambda Invoke: (Invokes Lambda by grabbing username,JWT token and Project Name) from sidecar container and Invokes lambda 
Process response.json:  Once Lambda invoked the response.json is processed to write to credentials file placed in /etc/.aws shared mount volume with compute. This in turn lets the user of the corresponding project gets access to the s3 bucket. 



Group policies for each projects can be created using the same template policy (porject_group_policy) 
Lambda policy to execute secrets (lambda_execution_role_permission) & associated assume policy
Service account Role policy that provides role to invoke lambda from the EKS cluster enabled with IRSA/OIDC (service_account_role) & associated assume policy
