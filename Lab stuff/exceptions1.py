try:
	amount = int(input("Enter the amount you wish to withdraw : "))
	print("Collect your cash")
except ValueError:
	print("Enter a proper amount")