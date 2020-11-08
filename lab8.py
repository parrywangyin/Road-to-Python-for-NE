from napalm import get_network_driver
import json
from getpass import getpass

ip = '172.16.209.85'
username = input('Username: ')
password = getpass('Password: ')

driver = get_network_driver('ios')
SW = driver(ip, username, password)
SW.open()
output = SW.get_interfaces()
#print (json.dumps(output, indent=2))

print ('\n交换机%s的下列端口的端口状态为up/up: \n' % (ip))
for key, value in output.items():
	if value['is_up'] == True:
		print (key + ',MAC地址为' + value['mac_address'])

