import paramiko
import os
import time
import logging
logging.basicConfig(level=logging.INFO)
ip = r'iplist.txt'
iplist=[line.strip() for line in open('iplist.txt')]
print(iplist)


def EsxCli(ipaddress):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	client.connect(hostname = ipaddress , port='22', username='root',password='VMware1!',look_for_keys=False)
	stdin,stdout,stderr = client.exec_command('/etc/init.d/vShield-Stateful-Firewall status')
	output_read = stdout.read()
	if 'vShield-Stateful-Firewall is running' in str(output_read):
		logging.info('\nService is already running!')
	elif 'vShield-Stateful-Firewall is not running' in str(output_read):
		logging.info('\nService is down, STARTING IT NOW')
		stdin, stdout, stderr = client.exec_command('/etc/init.d/vShield-Stateful-Firewall start')
		service_status = stdout.read()
		logging.info(str(service_status))
	else:
		logging.exception('SSH Timed OUT')

def StopVsfwd():
	for j in iplist:
		print(j)
		EsxCli(j)
StopVsfwd()
