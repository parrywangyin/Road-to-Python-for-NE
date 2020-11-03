import paramiko
import time
import getpass
import sys
import socket

username = input('Username: ')
password = getpass.getpass('password: ')
ip_file = sys.argv[1]
cmd_file = sys.argv[2]
 
switch_with_authentication_issue = []
switch_not_reachable = []
 
iplist = open(ip_file, 'r')
for line in iplist.readlines():
    try:
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip,username=username,password=password,look_for_keys=False)
        print ("已经成功登陆交换机", ip)
        command = ssh_client.invoke_shell()
        cmdlist = open(cmd_file, 'r')
        cmdlist.seek(0)
        for line in cmdlist.readlines():
            command.send(line + "\n")
        time.sleep(2)
        cmdlist.close()
        output = command.recv(65535).decode('ascii')
        print (output)
    except paramiko.ssh_exception.AuthenticationException:
        print (ip + "用户验证失败！")
        switch_with_authentication_issue.append(ip)
    except socket.error:
        print (ip +  "目标不可达！")
        switch_not_reachable.append(ip)
 
iplist.close()
ssh_client.close
 
print ('\n下列交换机用户验证失败：')
for i in switch_with_authentication_issue:
    print (i)
 
print ('\n下列交换机不可达：')
for i in switch_not_reachable:
    print (i)
