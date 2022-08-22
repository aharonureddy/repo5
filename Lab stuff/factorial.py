# write a function that returns the factorial of a number

def factorial(n):
	fact=1
	for i in range(1,n+1):
		fact = fact * i
	return fact


print(factorial(2) == 2)
print(factorial(3) == 6)

n = int(input("enter your number: "))
print(factorial(n))