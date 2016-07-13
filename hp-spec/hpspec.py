
# Goal: Generate list of equipment that needs ordering

# Make a list of the dictionaries
devicelist = []

# Define configuration

devicelist.append({'Model':'G9 DL360','CPU':'e1234','CPU Quantity':'1','CPU Max':'2','PSU Quantity':'500W','PSU Quantity':1,'PSU Max':2,'RAM Gb':4,'RAM Channels':4,'HDD Format':'SFF','HDD Quantity':1,'HDD Max':4,'Cost':1234})
devicelist.append({'Model':'G9 DL111','CPU':'e1111','CPU Quantity':'2','CPU Max':'4','PSU Quantity':'800W','PSU Quantity':1,'PSU Max':4,'RAM Gb':4,'RAM Channels':4,'HDD Format':'SFF','HDD Quantity':2,'HDD Max':4,'Cost':2341})
devicelist.append({'Model':'G9 DL999','CPU':'e9999','CPU Quantity':'1','CPU Max':'2','PSU Quantity':'500W','PSU Quantity':1,'PSU Max':4,'RAM Gb':4,'RAM Channels':4,'HDD Format':'SFF','HDD Quantity':2,'HDD Max':4,'Cost':4321})

cpulist = []
cpulist.append({'Model':'E1234 description'})
cpulist.append({'Model':'E2222 description'})
cpulist.append({'Model':'E9999 description'})

psulist = []
psulist.append({'Model':'500W description'})
psulist.append({'Model':'800W description'})

hddlist = []
hddlist.append({'Model':'1TB 15k description'})
hddlist.append({'Model':'300GB 15k description'})
hddlist.append({'Model':'500GB 7.5k description'})


# List models
entries=len(devicelist)
for configs in range(0,entries):
    print(configs,": ",devicelist[configs].get('Model'))

# Choose base system
ChoiceServer = int(input('Select your server: '))

# What is it fitted with
print('This server is fitted with ', devicelist[ChoiceServer].get('CPU Quantity'),'x',devicelist[ChoiceServer].get('CPU'))

# Different CPU?

# No of CPU
if(devicelist[ChoiceServer].get('CPU Quantity') < devicelist[ChoiceServer].get('CPU Max')):
    ChoiceCPUQuantity = int(input('Enter CPU quantity: '))

# Power
if(devicelist[ChoiceServer].get('PSU Quantity') < devicelist[ChoiceServer].get('PSU Max')):
    ChoicePSUQuantity = int(input('Enter PSU quantity: '))

# HDD quantity
if(devicelist[ChoiceServer].get('HDD Quantity') < devicelist[ChoiceServer].get('HDD Max')):
    ChoiceHDDQuantity = int(input('Enter HDD quantity: '))

# List out all the HDD types
entries=len(hddlist)
for configs in range(0,entries):
    print(configs,": ",hddlist[configs].get('Model'))
ChoiceHDDType = int(input('Enter HDD type: '))

# Calculate RAM
print(' ')
print('ChoiceCPUQuantity',ChoiceCPUQuantity)
print('ChoicePSUQuantity',ChoicePSUQuantity)
print('ChoiceCPUQuantity',ChoiceCPUQuantity)
print('ChoiceHDDQuantity',ChoiceHDDQuantity)
print('ChoiceHDDType',ChoiceHDDType)
