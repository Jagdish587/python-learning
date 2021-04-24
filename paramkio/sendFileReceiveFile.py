import paramiko 

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname="linux-machine ip",username="jagdish",password="1234")


stdin,stdout,stderr=ssh_client.exec_command("sudo apt-get update")
stdin.write("1234\n")

stdin,stdout,stderr=ssh_client.exec_command("pwd")
print(stdout.readlines())
stdin,stdout,stderr=ssh_client.exec_command("touch createFromVSCode.txt")
stdin,stdout,stderr=ssh_client.exec_command("echo \"Hi ,I am from VSCode\">>createFromVSCode.txt")

# Download file from remote machineftp_client=ssh_client.open_sftp()
ftp_client=ssh_client.open_sftp()
ftp_client.get("/home/jagdish/createFromVSCode.txt","createFromVSCode.txt")


#Send File from send local machine to remote machine
ftp_client.put("mystuff.py","/home/jagdish/mystuff.py")
ftp_client.close()
