from napalm import get_network_driver
from getpass import getpass

ip = '192.168.2.11'
username = input('Username: ')
password = getpass('Password: ')

driver = get_network_driver('ios')
SW = driver(ip, username, password)
SW.open()

SW.load_merge_candidate(filename='napalm_config.cfg')
SW.commit_config()
