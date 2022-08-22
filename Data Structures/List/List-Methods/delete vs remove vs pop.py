'''
pop:
pop takes index and returns values
it delete only one item
it is a postfix method

delete:
it takes index, removes value at the index, and return nothing
it is a prefix method
it delete multiple values

remove:
remove takes value and removes first occurreance, and return nothing
it delete only one item
'''

lst1 = [10,20,20,30,30,35,25]
lst1.remove(30)
print(lst1)

lst2 = [10,25,40,30,80,35,25]
lst2.pop(1)
print(lst2)

lst3 = [15,26,40,35,80,30,45]
del lst3[0]
print(lst3)
lst3 = [15,26,40,35,80,30,45]
del lst3[3:]
print(lst3)

'''
output:
[10, 20, 20, 30, 35, 25]
[10, 40, 30, 80, 35, 25]
[26, 40, 35, 80, 30, 45]
[15, 26, 40]
'''

