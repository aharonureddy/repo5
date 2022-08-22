# Create a script which accepts a number and 
# prints the multiplication table of the number  
# in the format '1 X n = n' and so on up to '12 X n ='

num=int(input("Enter number for multiplication table: "))

for count in range(1,13):
    print("{} X {} = {}".format(count,num,count*num))
