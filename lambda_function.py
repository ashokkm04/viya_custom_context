import boto3
import json

secrets_client = boto3.client('secretsmanager')

def lambda_handler(event, context):
    # Extract parameters from the event
    project_id = event.get('project')
    username = event.get('username')
    jwt = event.get('jwt')

    # Determine the secret name based on project_id
    if project_id == 'hr':
        secret_name = 'hr_secret'
    elif project_id == 'sales':
        secret_name = 'sales_secret'
    elif project_id == 'marketing':
        secret_name = 'marketing_secret'
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid project_id'})
        }

    # Retrieve the secret from Secrets Manager
    try:
        response = secrets_client.get_secret_value(SecretId=secret_name)
        secret = json.loads(response['SecretString'])

        # Print the entire secret for debugging
        print(f"Retrieved secret: {secret}")

        # Extract the credentials from the secret based on actual key names
        access_key = secret.get('access_key')
        secret_key = secret.get('secret_key')

        # Check if credentials were retrieved correctly
        if access_key and secret_key:
            # Return the credentials in the specified response format
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'AccessKeyId': access_key,
                    'SecretAccessKey': secret_key,
                    'SessionToken': None  # If you have a session token, include it here
                })
            }
        else:
            # Return error if any credentials are missing
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'Missing credentials in the secret'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Error retrieving credentials: {str(e)}'})
        }