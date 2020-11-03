import paramiko
import time
import getpass

username = input('Username: ')
password = getpass.getpass('Password: ')

f = open('ip_list.txt')

for line in f.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password, look_for_keys=False)
    command = ssh_client.invoke_shell()
    print ('已经成功登录交换机 ' + ip)
    command.send('conf terminal\n')
    command.send('router eigrp 1\n')
    time.sleep(0.5)
    command.send('end\n')
    command.send('wr mem\n')
    time.sleep(2)
    output = command.recv(65535).decode('ASCII')
    print (output)

f.close()
ssh_client.close
