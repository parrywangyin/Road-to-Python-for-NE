from netmiko import ConnectHandler
import schedule

def backup_config():
    f = open('ip_list.txt')
    for ips in f.readlines():
        ip = ips.strip()
        device = {'device_type': 'cisco_ios', 'host':ip, 'username': 'python', 'password': '123'}
        ssh_client = ConnectHandler(**device)
        output = ssh_client.send_command('show run')
        backup = open(ip + '.txt', 'a+')
        backup.write(output)
        backup.close()
        print (f'交换机{ip}配置已备份完毕')
    f.close()

schedule.every(5).seconds.do(backup_config)

while True:
  schedule.run_pending()
