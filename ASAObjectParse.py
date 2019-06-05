import ntpath
import netmaskdictionary

# Input the file in full directory format, IE: C:\temp\file.txt
fileLocation = input("Location of ASA Object Configuration: ")
fileDir = ntpath.dirname(fileLocation)

# Import Dictionary of netmasks in CIDR
netmaskDict = netmaskdictionary.netmaskDict

# Read the document into a List
asaConfigFile = open(fileLocation, "r")
row = [line.split(' ') for line in asaConfigFile.readlines()]
asaConfigFile.close()

# Pull out the first line to get the tag and address-group name, then remove it from the list
group = row[0]
del row[0]
print(group)
name = group[2].strip('\n')

# Check for description and add if it exists
if "description" in row[0][1]:
    description = row[0][1]
    del row[0]
else:
    description = ""

objects = []
for items in row:
    address = []
    for i in range (1, 4):
        address.append(items[i])
    objects.append(address)

setAddress = []
for items in objects:
    if items[1] == "host":
        addr = items[2].strip('\n')
        setAddress.append("set address IP-"+addr+" tag "+name+" ip-netmask "+addr+"\n")
    else:
        addr = items[1]
        netmask = items[2].strip('\n')
        netmask = netmaskDict[netmask]
        setAddress.append("set address IP-"+addr+" tag "+name+" ip-netmask "+addr+netmask+"\n")

with open(fileDir+"\\"+name+"-palo.txt", "w+") as file_handler:
    file_handler.write("set tag "+name+"\n")
    file_handler.write("set address-group "+name+" dynamic filter '"+name+"'\n")
    for item in setAddress:
        file_handler.write("{}".format(item))
