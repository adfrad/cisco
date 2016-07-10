# generate.py
# this file will ask which template and generate a config
#

#!/usr/bin/env python3
import fileinput
import re #regex handler
import check_ip_legit #ip legitimacy checker

'''
#Dictionary containing files, inputs
templateOptions = {}
templateOptions['FileLocation': './templates/5515x-template-single-network.txt' , 'Description': 'Single NIC']
templateOptions['FileLocation': './templates/5515x-template-double-network.txt' , 'Description': 'Double NIC']
templateOptions['FileLocation': './templates/5515x-template-triple-network.txt' , 'Description': 'Triple NIC']



for x in count(templateOptions):
    print (templateOptions['Description'])
'''

fileToSearch = r'./templates/5515x-template-single-network.txt'
fileToSave = open('output.txt',"w")

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
