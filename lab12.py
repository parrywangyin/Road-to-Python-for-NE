import json
from pyntc import ntc_device as NTC

SW = NTC(host='192.168.2.11', username='python', password='123', device_type='cisco_ios_ssh')
SW.open()

#print (json.dumps(SW.facts, indent=4))
SW.config('hostname pyntc_S1')
SW.config_list(['router ospf 1', 'network 192.168.2.0 0.0.0.255 area 0'])

SW.close()
