lst1 = [10,20,30,10,40,60,70,80,40]
print(lst1)
del lst1[len(lst1)-1]   # delete last index element
print(lst1)

del lst1[round(len(lst1)/2)]  # delete middle element
print(lst1)

# delete using slice operator
del lst1[3:]
print(lst1)

# Example, delete min element in the list
lst2 = [10,30,40,10,20,40,5]
print(lst2)
idx =-1
for i in lst2:
    idx+=1
    if min(lst2)==lst2[idx]:
        del lst2[idx]
print(lst2)
