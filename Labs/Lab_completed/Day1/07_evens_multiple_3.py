# Accept numbers from the user until he enters 0. Print back the numer if it is an even number divisible by 3

while True:
    num=int(input("Enter number (enter 0 to stop) : "))
    if num==0:
        break
    if num%2==0 and num%3==0:
        print(num)
