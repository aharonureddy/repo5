def divide(a,b):
	try:
		result = a/b
		print(result)
	except ZeroDivisionError:
		print("Check your denominator")
	except TypeError:
		print("Only numbers allowed")


divide(5,2)
divide(5,0)
divide(5,'a')