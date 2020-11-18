import telnetlib

host = '192.168.2.11'
user = 'python'
password = '123'

tn = telnetlib.Telnet(host)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b'\n')
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b'\n')

print ('已经登录交换机' + host)
tn.write(b"conf t\n")
tn.write(b"inter loopback 1\n")
tn.write(b"ip add 11.11.11.11 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"wr mem\n")
tn.write(b"exit\n")

output = tn.read_all().decode('ascii')
print (output)

