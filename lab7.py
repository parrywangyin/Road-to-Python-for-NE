from pythonping import ping

for i in range(11,17):
	ip = '192.168.2.' + str(i)
	result = ping(ip)
	if 'Reply' in str(result):
		print (ip +'可达')
	else:
		print (ip +'不可达')
