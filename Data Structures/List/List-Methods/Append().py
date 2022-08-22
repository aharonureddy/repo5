# append method is used for adding a single value at the end of the list
# example:
lst1 = [1,2,3,4,5]
lst1.append(6)
print(lst1)

# example: common element to add another list
print("------------------------")
lst2 = [10,20,50,30,60,70]
lst3 = [20,50,40,30,70,80,90]
lst4=[]                # empty list for storing common elements
for i in lst2:
    for j in lst3:
     if i==j:
         lst4.append(i)
print(lst4)


# example: To add all elements to list up to 50 which are divisible by 10
print("------------------------")
list =[]
for i in range(51):
    if i % 10 == 0:
        list.append(i)
print(list)