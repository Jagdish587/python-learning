import paramiko 

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname="ip-address",username="jagdish",password="1234")


stdin,stdout,stderr=ssh_client.exec_command("pwd")

print(stdout.readlines())


