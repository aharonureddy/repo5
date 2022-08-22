# example
lst1 = [10,20,30]
lst2 = [30,40,10]
lst3 = lst1 + lst2
print(lst3)


# example
print("=============")
lst4 = [20,4,5,6]
lst5 = [2,30,4,21]
lst6=lst4
print(lst4)
print(lst5)
print("-----------------")
for i in range(len(lst4)):
    lst6[i] = lst4[i]+lst5[i]
print(lst6)
