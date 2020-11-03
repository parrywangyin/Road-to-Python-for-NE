from netmiko import ConnectHandler

S2 = {'device_type': 'cisco_ios', 
      'ip': '192.168.2.12',
      'username': 'python',
      'password': '123'}

connect = ConnectHandler(**S2)
print ('已经成功登录交换机' + S2['ip'])
config_commands = ['int loop 1', 'ip add 2.2.2.2 255.255.255.255']
output = connect.send_config_set(config_commands)
print (output)
result = connect.send_command('show run int loop 1')
print (result)
