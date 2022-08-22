#DocString


def add(a,b):
	"""this function takes two numbers
	and returns their sum"""
	return a+b

help(add)


#Call by reference

a=[1,2,3,4]

def destroy(x):
	print(x.pop())

print(a)
destroy(a)
print(a)


#Call by value

print(a)
destroy(a[:])
print(a)

#Variable number of parameters

def total(*args):
	print(sum(args))

total(3,4)
total(3,4,5)
total(45,6,7,8,9,3,4,5,6)