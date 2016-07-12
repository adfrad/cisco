
# Goal: Generate list of equipment that needs ordering

# Make a list of the dictionaries
devicelist = []

# Define configuration

devicelist.append({'Model':'G9 DL360','CPU':'e1234','CPU Quantity':'1','PSU Power':'500W','PSU Quantity':'1','RAM Gb':4,'RAM Channels':'4','HDD Format':'SFF','HDD Slots':4})
devicelist.append({'Model':'G9 DL999','CPU':'e9999','CPU Quantity':'1','PSU Power':'500W','PSU Quantity':'1','RAM Gb':4,'RAM Channels':'4','HDD Format':'SFF','HDD Slots':4})




# Choose base system
#print(devicelist)
#print('')
#print(devicelist[0].get('CPU'))

print(len(devicelist))
entries=len(devicelist)
for configs in range(0,entries):
    print(configs,": ",devicelist[configs].get('Model'))
#    print(devicelist[configs].get('Model'))


# Different CPU?

# No of CPU

# Power

# HDD

# Calculate RAM
