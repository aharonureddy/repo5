# The clear() method removes all the items from the list. It equivalent "del list[:]"

lst1 = [10,20,30,35,40]
lst1.clear()
print(lst1)

lst2 = [14,10,34,35,40]
del lst2[:]
print(lst2)

'''
output:
[]
[]
'''


