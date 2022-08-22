# The extend method is used for adding a multiple values at the end of the list
# example:
lst1 = ['nit','nacre']

lst1.extend('Aharonu IT')     # string as iterable object ( can't pass this type)
print(lst1)
# output: ['nit', 'nacre', 'A', 'h', 'a', 'r', 'o', 'n', 'u', ' ', 'I', 'T']

lst1.extend(['Aharonu IT'])
print(lst1)
# output : ['nit', 'nacre', 'Aharonu IT']


# example:
print("-----------")
lst2=[1,2,3,4,5,6]
lst3 = ["Python", "Datascience"]
lst2.extend(lst3)
print(lst2)
#output: [1, 2, 3, 4, 5, 6, 'Python', 'Datascience']

# example:
print("-----------")
l= [1,2,3]
ll = [4,5,6]
l.extend(ll)
print(l)
# output: [1, 2, 3, 4, 5, 6]