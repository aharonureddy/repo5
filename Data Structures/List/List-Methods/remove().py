# The remove() method takes single argument, the item which is to be removed.
# it removes the first occurrence of the given item in the list and returns an error if the time is not present


y= ['Python',1,2,3,4]
y.remove(4)
print(y)

ll = [2,'Aharonu',12.5]
ll.remove(2)
print(ll)

lst1 = [10,20,30,40,60]
lst1.remove(lst1[round(len(lst1)/2)])
print(lst1)

'''
output:
['Python', 1, 2, 3]
['Aharonu', 12.5]
[10, 20, 40, 60]

'''