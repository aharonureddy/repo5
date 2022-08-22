# The insert method is used to insert an item into the list at a required position.
# It takes two values arguments, index position and value to be inserted

lst1 = [1,2,3,4,5]
lst1.insert(0,"Python")
print(lst1)


lst2=[10,20,30,40]
lst2.insert(-1,50)
print(lst2)


lst3 = [10,20,30,40,50]
lst3.insert(round(len(lst3)/2),35)    # insert middle
print(lst3)

lst4 = [10,20,30,40,50]
lst4.insert(0,5)
print(lst4)

n=[1,2,3,4]
n.insert(1,888)
print(n)

'''
output:
['Python', 1, 2, 3, 4, 5]
[10, 20, 30, 50, 40]
[10, 20, 35, 30, 40, 50]
[5, 10, 20, 30, 40, 50]
[1, 888, 2, 3, 4]
'''