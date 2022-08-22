# Deleting a tuple, it is not possible to delete individual elements of a tuple. We can delete the whole tuple itself by using "del" statement

tup1 = ("nit","python")
print(tup1)
del tup1
print(tup1)
# output : NameError: name 'tup1' is not defined. Did you mean: 'tuple'?

# in above program, we can delete items

tup2 = ("nit","python")
print(tup2)
tup2=tuple()
print(tup2)
# ()


