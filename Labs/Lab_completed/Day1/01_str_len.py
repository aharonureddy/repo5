# accept a name and print the length of the name. If name is blank print an error message 'please enter a valid value'

name=input("Enter name : ")
if len(name)==0:
    print("Please enter a valid name")
else:
    print(len(name))
