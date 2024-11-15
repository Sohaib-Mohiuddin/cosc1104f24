import paramiko

def ssh_to_ec2(instance_ip, key_file_path):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the instance
        ssh.connect(hostname=instance_ip, username='ec2-user', key_filename=key_file_path)
        print("Connected to the instance")

        # Execute a command
        stdin, stdout, stderr = ssh.exec_command('uname -a')
        print("Command output:", stdout.read().decode())

    except Exception as e:
        print(f"Error connecting to the instance: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    instance_ip = 'YOUR_INSTANCE_PUBLIC_IP'
    key_file_path = 'path/to/your/private-key.pem'
    ssh_to_ec2(instance_ip, key_file_path)