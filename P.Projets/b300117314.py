"""
Created on Mon Mar 16 13:09:48 2020

@author: Morti
"""
"""
Created on Mon Mar 16 13:09:48 2020

@author: Morti
"""

import getpass
import sys
import telnetlib

HOST = "192.168.163.154"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loop 3\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("int loop 4\n")
tn.write("ip address 2.2.2.2 255.255.255.255\n")
tn.write("router ospf 1\n")
tn.write("network 0.0.0.0 255.255.255.255 area 0\n")
tn.write("end\n")
tn.write("exit\n")

print (tn.read_all())
