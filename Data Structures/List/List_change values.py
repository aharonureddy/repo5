'''
# we can change values of list elements
lst1 = [10,20,30,40,50]
lst1[2] = 35
'''

# example1: can max element in the list
lst1 = [10,20,30,60,50]
idx=-1
print(lst1[idx])
for i in lst1:
    idx+=1
    if max(lst1) == lst1[idx]:
        lst1[idx] = 100
print("after change")
print(lst1)





