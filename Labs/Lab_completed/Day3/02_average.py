# Create and test a function which accepts any number of numbers
# and print the average of the numbers

# Defining the function

def average(*nums):
    """Function to return the average of given numbers."""
    avg=sum(nums)/len(nums)
    return avg


# Invoking the function
#first=int(input("Enter a number : "))
#second=int(input("Enter a number : "))
#third=int(input("Enter a number : "))

nums=[45,34,46,65,33,55]
result = average(*nums)
print(result)
