# Create and test a function which accepts three numbers
# and print the average of the numbers

# Defining the function
def average_of_3(n1,n2,n3):
    avg=(n1+n2+n3)/3
    return avg


# Invoking the function
first=int(input("Enter a number : "))
second=int(input("Enter a number : "))
third=int(input("Enter a number : "))

result = average_of_3(first,second,third)
print(result)
