import ntpath

# Input the file in full directory format, IE: C:\temp\file.txt
fileLocation = input("Location of ASA Object Configuration: ")

fileDir = ntpath.dirname(fileLocation)

asaConfigFile = open(fileLocation, "r")
row = [line.split(' ') for line in asaConfigFile.readlines()]
asaConfigFile.close()

netmaskDict = {
    "0.0.0.0": "/0",
    "255.0.0.0": "/8",
    "255.128.0.0": "/9",
    "255.192.0.0": "/10",
    "255.224.0.0": "/11",
    "255.240.0.0": "/12",
    "255.248.0.0": "/13",
    "255.252.0.0": "/14",
    "255.254.0.0": "/15",
    "255.255.0.0": "/16",
    "255.255.128.0": "/17",
    "255.255.192.0": "/18",
    "255.255.224.0": "/19",
    "255.255.240.0": "/20",
    "255.255.248.0": "/21",
    "255.255.252.0": "/22",
    "255.255.254.0": "/23",
    "255.255.255.0": "/24",
    "255.255.255.128": "/25",
    "255.255.255.192": "/26",
    "255.255.255.224": "/27",
    "255.255.255.240": "/28",
    "255.255.255.248": "/29",
    "255.255.255.252": "/30",
    "255.255.255.254": "/31",
    "255.255.255.255": "/32"
}

#Pull out the first line to get the tag and address-group name, then remove it from the list
group = row[0]
del row[0]
name = group[2].strip('\n')

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
