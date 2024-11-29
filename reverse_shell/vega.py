import paramiko
import getpass

hostname = '192.168.0.32'
port = 22

# Prompt for username and password
username = input("Enter your SSH username: ")
password = input("Enter your SSH password: ")

# Initialize SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server
try:
    ssh.connect(hostname, port, username, password)
    print("Connected successfully!")

    while True:
        command = input("Enter the command to execute (or 'exit' to close): ")
        if command.lower() == 'exit':
            break
        stdin, stdout, stderr = ssh.exec_command(command)
        print("Output:")
        print(stdout.read().decode())
        print("Errors:")
        print(stderr.read().decode())

except paramiko.AuthenticationException:
    print("Authentication failed.")
except paramiko.SSHException as sshException:
    print(f"Unable to establish SSH connection: {sshException}")
except Exception as e:
    print(f"Exception: {e}")

# Close the connection
finally:
    ssh.close()
    print("Connection closed.")

