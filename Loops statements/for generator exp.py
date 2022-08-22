# example, display the first 10 natural numbers squares  by using generator expression


for x in (x**2 for x in range(10)):
    print(x)


