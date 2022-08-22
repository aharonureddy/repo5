# The pop() method removes and returns the item from the list
# if no index is specified, list.pop() removes and returns the last itme in the list.

x=[11,21,58,2,6,78,9,5]
print(x.pop())      # it deletes last index item '5'
print(x)

lst1 = [10,20,30,40,50]
lst1.pop(round(len(lst1)/2))   # delete middle index item
print(lst1)

lst2=[10,20,30,40,50]
lst2.pop(0)                   # delete first index '10'
print(lst2)