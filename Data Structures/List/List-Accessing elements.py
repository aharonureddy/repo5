# accessing elements - using indexing a list
list1=[10,20,30,40,50]

print(list1[1])    # 20
print(list1[-5])    #10
print(list1[1+2])   # list1[3] by operator

# accessing elements - using loops
# using for loop
print("using for loop")
list2 = [10,20,30,40]
for i in list2:
    print(i)


# using while loop
print("using while loop")
list3 = [10,20,30,40,50]
i=0
while i < len(list3):
    print(list3[i])
    i+=1


