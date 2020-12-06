from pyntc import ntc_device as NTC

SW = NTC(host='192.168.2.11', username='python', password='123', device_type='cisco_ios_ssh')
SW.open()

SW.backup_running_config('S1_config.cfg')
SW.close()
