import getpass
import paramiko
import time

BUFF_SIZE = 65535

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input('Username: ')
pwd = getpass.getpass('Password: ')

cli.connect('114.71.220.5', username=user, password=pwd)
channel = cli.invoke_shell() 

channel.send('cat /proc/cpuinfo\n') 
time.sleep(0.5)

channel.send('cat /proc/meminfo\n')
time.sleep(0.5)

channel.send('mkdir -p test\n')
time.sleep(0.5)

channel.send('cd test\n')
time.sleep(0.5)

channel.send('echo iot > iot.txt\n')
time.sleep(0.5)

channel.send('cat iot.txt\n')
time.sleep(0.5)

output = channel.recv(BUFF_SIZE).decode() 
print(output)

cli.close()
