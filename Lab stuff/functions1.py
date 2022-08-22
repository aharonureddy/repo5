#Defining Function

def hi():
	print("Good morning")

hi()

#Processing parameters

def hello(name):
	print("How are you {}".format(name))

hello("wells fargo")

def wish(name, age):
	print("Hello {} your age is {} years".format(name, age))

wish("India", 75)

#The return statements

def square(x):
	return x*x

result = square(56)
print(square(4))
k = square(34) + square(23) + square(square(2))
print(k)

def add(a,b):
	return a+b

print(add(3,4))

#Local Variables

def circle_area(radius):
	pi = 3.14 # local variable
	return pi * radius * radius

print(circle_area(45))

#Keyword Arguments

wish(75, 'India')

wish(age=75, name='India')

