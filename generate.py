# generate.py
# this file will ask which template and generate a config

#!/usr/bin/env python3
import fileinput
#import ipaddress #ip address handler
import re #regex handler
#import io
#import sys
import check_ip_legit #ip legitimacy checker

fileToSearch = r'C:\Users\adam\Documents\GitHub\cisco\templates\5515x-template-single-network.txt'
fileToSave = open(r'C:\Users\adam\Documents\GitHub\cisco\templates\output.txt',"w")

inside_ip = "256.1.1.1" #force a prompt in the while loop by giving bad address
outside_ip = "256.1.1.1" #force a prompt in the while loop by giving bad address

while (check_ip_legit.is_valid_ip(inside_ip) == False): #keep prompting until a valid IP address is given
    inside_ip = input('Input INSIDE IP address: ')
while (check_ip_legit.is_valid_ip(outside_ip) == False): #keep prompting until a valid IP address is given
    outside_ip = input('Input OUTSIDE IP address: ')

for line in open(fileToSearch,'r'):
#    newline = line.replace('<external_ip>', outside_ip)
    if '<external_ip>' in line:
        newline = line.replace('<external_ip>', outside_ip)
    elif '<internal_ip>' in line:
        newline = line.replace('<internal_ip>', inside_ip)
    else:
        newline = line
    fileToSave.write(newline)
