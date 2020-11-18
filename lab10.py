from napalm import get_network_driver
from getpass import getpass

ip = '192.168.2.11'
username = input('Username: ')
password = getpass('Password: ')

driver = get_network_driver('ios')
SW = driver(ip, username, password)
SW.open()

SW.load_merge_candidate(filename='napalm_config.cfg')
differences = SW.compare_config()
print (differences)

if len(differences)>0:
	SW.commit_config()
else:
	print('不需要做配置')
	SW.discard_config()
