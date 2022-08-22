# Create a class called Person. The attributes are name, address, contact_no
# Add appropriate methods to access these values
# Create objects and test the class


class Person:
    def __init__(self,name,addr,contact):
        self.name=name
        self.address=addr
        self.contact_no=contact

    def getName(self):
        return self.name
    def getContact(self):
        return self.contact_no
    def getAddress(self):
        return self.address
    def setContact(self,contact):
        self.contact_no=contact
    def setAddress(self,addr):
        self.address=addr
    def __repr__(self):
        return f"Name: {self.name}, Address : {self.address}, Contact_no : {self.contact_no}"



# Create objects

ram = Person('Ram Kumar','Westside','11111')
print(ram)

print(ram.getAddress())
ram.setContact(22222)
print(ram)

    
