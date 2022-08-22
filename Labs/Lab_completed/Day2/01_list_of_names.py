# Create an empty list for storing names. Accept names from the user and store them in the list in upper case.
# Finally print the names in the list in sorted order.

# Create empty list

names=[]

#for count in range(5):

while True:
    name=input("enter name: ")
    if len(name)==0:
        break
    names.append(name.upper())

print(names)

# Sorting the names
names.sort()
print(names)
