import boto3
import time

def run_command_on_ec2(instance_id, command):
    # Create an SSM client
    ssm_client = boto3.client('ssm')

    # Send the command to the EC2 instance
    response = ssm_client.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': [command]}
    )

    command_id = response['Command']['CommandId']
    print(f"Command sent. Command ID: {command_id}")

    # Wait for the command to complete
    time.sleep(2)  # Wait a moment for the command to start

    # Retrieve the command output
    output_response = ssm_client.list_command_invocations(
        CommandId=command_id,
        Details=True
    )

    for invocation in output_response['CommandInvocations']:
        for result in invocation['CommandPlugins']:
            print(f"Output: {result['Output']}")

if __name__ == "__main__":
    instance_id = 'YOUR_INSTANCE_ID'  # Replace with your EC2 instance ID
    command = 'echo "Hello from EC2!"'  # Replace with your command
    run_command_on_ec2(instance_id, command)