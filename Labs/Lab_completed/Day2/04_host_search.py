# Create a dictionary with host names and corresponding IP addresses. Add code to allow searching in the dictonary. If the searched hostname is not in the dictionary, print an error message.

hosts={'Linux':'192.168.2.1','Windows10':'192.168.2.22','Oracle':'192.168.2.2'}

host=input("Enter host name: ")

ipaddr=hosts.get(host.title())

if ipaddr:
    print("IP Address is :",ipaddr)
else:
    print("Sorry, not in the database")
