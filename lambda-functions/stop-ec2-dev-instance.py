import boto3

def lambda_handler(event, context):
    print("Starting Lambda function execution...")
    
    # Initialize the EC2 client
    print("Initializing EC2 client...")
    ec2_client = boto3.client('ec2')
    
    # Define the tag key-value pair to filter instances
    tag_key = 'env'
    tag_value = 'dev'
    
    try:
        print("Describing EC2 instances with the specified tag...")
        # Describe EC2 instances with the specified tag
        response = ec2_client.describe_instances(
            Filters=[
                {'Name': 'instance-state-name', 'Values': ['running']},
                {'Name': f'tag:{tag_key}', 'Values': [tag_value]}
            ]
        )
        
        # Check if there are running instances with the specified tag
        if 'Reservations' in response and len(response['Reservations']) > 0:
            print("Running instances found with the specified tag. Printing details...")
            # Iterate over reservations and stop instances
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    instance_type = instance['InstanceType']
                    private_ip = instance['PrivateIpAddress']
                    print(f"Stopping instance: {instance_id}, Type: {instance_type}, Private IP: {private_ip}")
                    # Stop the instance
                    ec2_client.stop_instances(InstanceIds=[instance_id])
                    
                    # Wait until instance state changes to stopped
                    waiter = ec2_client.get_waiter('instance_stopped')
                    waiter.wait(InstanceIds=[instance_id])
                    
                    print(f"Instance {instance_id} stopped successfully.")
        else:
            print("No running instances found with the specified tag.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Lambda function execution completed.")

# Uncomment the line below for testing locally
# lambda_handler(None, None)

