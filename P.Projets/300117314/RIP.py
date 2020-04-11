
"""
Created on Sun Mar 22 17:05:52 2020

@author: Morti
"""


import getpass
import sys
import telnetlib
import time

Host="192.168.163.158"

user=input(' Enter User name: ')
password=getpass.getpass()

tn = telnetlib.Telnet(Host)
tn.read_until(b'Username: ')
tn.write(user.encode('ascii') + b'\n')

if password:
    tn.read_until(b'Password: ')
    tn.write(password.encode('ascii')+b'\n')
time.sleep(2)
tn.write(b'enable\n')
time.sleep(2)
tn.write(b'cisco\n')
time.sleep(2)
tn.write(b'config t\n')
time.sleep(2)
tn.write(b'router rip\n')
time.sleep(2)
tn.write(b'network 192.168.10.0 \n')
time.sleep(2)
tn.write(b'no auto-summary\n')
time.sleep(2)
tn.write(b'version 2\n')
time.sleep(2)


tn.write(b'end\n')
tn.write(b'exit\n')
line=tn.read_all()
print (line)