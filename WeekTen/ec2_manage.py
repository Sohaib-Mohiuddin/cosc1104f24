import boto3

def connect_to_ec2():
    # Create a session using your AWS credentials
    session = boto3.Session(
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY',
        region_name='YOUR_REGION'  # e.g., 'us-east-1'
    )

    # Create an EC2 resource
    ec2 = session.resource('ec2')

    # Optionally, you can filter instances based on specific criteria
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    # Print information about each running instance
    for instance in instances:
        print(f'Instance ID: {instance.id}')
        print(f'Instance Type: {instance.instance_type}')
        print(f'Public IP: {instance.public_ip_address}')
        print(f'State: {instance.state["Name"]}')
        print('---')

if __name__ == "__main__":
    connect_to_ec2()