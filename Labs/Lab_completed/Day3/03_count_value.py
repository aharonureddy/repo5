# Create and test a function which accepts a dictionary and a value.
# The function should return the count of the given value in the dictionary.
# Try callng the function using keyword arguments.


def count(d,v):
    """Function to return the number of occurrences
        of the given value 'v' n the dctionary 'd'."""

    values=list(d.values())
    return values.count(v)



# using the function

marks={'mary':90,
       'joy':85,
       'meera':82,
       'anil':85,
       'ravi':85,
       'sheela':82}

searchmark = int(input("Enter search mark : "))
num = count(marks,searchmark)

print("{} students scored {}".format(num,searchmark))
    
