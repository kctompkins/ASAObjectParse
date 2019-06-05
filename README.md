# ASAObjectParse
Parse ASA Object-Groups into Palo Alto Set commands

Input a text file that is an ASA configuration for an object-group containing a number of IP address entries. The script will output a text file that is Palo Alto set commands to create a dynamic address-group and addresses that match the original object-group.

Please refer to the example_input.txt file for formatting of the original entry. Note that a combination of host type network-objects and IP/netmask type network-objects is supported.