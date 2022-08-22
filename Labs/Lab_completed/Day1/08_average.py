# Accept numbers from the user until the user enters 0 and print the average of the numbers. 

count=sum=0

while True:
    num=int(input("Enter number (enter 0 to stop) : "))
    if num==0:
        break
    sum = sum+num
    count = count+1

avg=sum/count
print("Average : ",avg)
