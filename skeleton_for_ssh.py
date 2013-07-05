#!/opt/local/bin/python2.7
#
# This is a simple skeleton file for connecting to hosts with python.
# Fill in hosts, username, keyfile and commands below. 
# If you want to use password for connecting to host instead of key, use 
# ssh.connect(i, username='<user>', password='<password>'), but keep in 
# mind hthat keeping passwords in plain text is a very bad idea. 
# In this example, if the first parameter given is show, the first command 
# is ran, in any other case the second one. 

import paramiko
import sys


hosts="list_of_hosts"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for i in hosts.split( ):
    print i
    ssh.connect(i, username='user', key_filename='/path/to/key/file')

    print sys.argv[1]
    if sys.argv[1] == "show":
        stdin, stdout, stderr = ssh.exec_command("uptime; df -h")
    else:
        stdin, stdout, stderr = ssh.exec_command("echo 'run here another \
                                    command'")
    type(stdin)
    for j in stdout.readlines():
        print j
    ssh.close()
