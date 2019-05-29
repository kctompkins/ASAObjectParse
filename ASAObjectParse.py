import ntpath

# Input the file in full directory format, IE: C:\temp\file.txt
fileLocation = input("Location of ASA Object Configuration: ")

fileDir = ntpath.dirname(fileLocation)
print(fileDir)

asaConfigFile = open(fileLocation, "r")
row = [line.split(' ') for line in asaConfigFile.readlines()]
asaConfigFile.close()

group = row[0]
del row[0]
print(group)

objects = []
for items in row:
    address = []
    for i in range (1, 4):
        address.append(items[i])
    objects.append(address)
print(objects)

with open(fileDir+r"\address-group.txt", "w+") as file_handler:
    for item in objects:
        file_handler.write("{}\n".format(item))
