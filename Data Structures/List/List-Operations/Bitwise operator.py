# we can perform only integer values. We can't perform entire list and string other objects
# example:

lst1 = [1,2,3]
lst2 = [4,3,2]
lst3 = lst1
print(lst1)
print(lst2)
print("---------------")
idx=-1
for i in range(len(lst1)):
    idx+=1
    lst3[idx]=lst1[idx] | lst2[idx]
print(lst3)

'''
output:
[1, 2, 3]
[4, 3, 2]
---------------
[5, 3, 3]
'''