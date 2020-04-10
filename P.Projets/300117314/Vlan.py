"""
Created on Sun Mar 22 17:05:52 2020

@author: Morti
"""

import getpass
import sys
import telnetlib
import time

Host="192.168.163.150"

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

tn.write(b'vlan 20\n')
tn.write(b'name Accounting\n')
time.sleep(2)
tn.write(b'int vlan 20\n')
time.sleep(2)
tn.write(b'ip add 20.20.20.20 255.255.255.0\n')

tn.write(b'vlan 30\n')
tn.write(b'name Human_resource\n')
time.sleep(2)
tn.write(b'int vlan 30\n')
time.sleep(2)
tn.write(b'ip add 30.30.30.30 255.255.255.0\n')

tn.write(b'vlan 40\n')
time.sleep(2)
tn.write(b'name Marketing\n')
time.sleep(2)
tn.write(b'int vlan 40\n')
time.sleep(2)
tn.write(b'ip add 40.40.40.40 255.255.255.0\n')

tn.write(b'name Finance\n')
time.sleep(2)
tn.write(b'int vlan 50\n')
time.sleep(2)
tn.write(b'ip add 50.50.50.50 255.255.255.0\n')

tn.write(b'end\n')
tn.write(b'exit\n')
line=tn.read_all()
print (line)

 

