# example:
lst1 = [1,2,3,4]
lst2 = [5,6,7]
lst1.append(lst2)
print(lst1)

lst3 = [1,2,3,4]
lst4 = [5,6,7]
lst1.extend(lst3)
print(lst3)

'''output:
[1, 2, 3, 4, [5, 6, 7]]
[1, 2, 3, 4]
'''

# exaple: Using + operator are equivalent ot append and extend method
print("----------")
lst5=[10,20,30]
lst6=[40,50]
lst7=lst5 + [lst6]      # append method
print(lst7)

lst8=[20,30,40]
lst9=[50,60]
lst10 = lst8 + lst9
print(lst10)

'''output:
[10, 20, 30, [40, 50]]
[20, 30, 40, 50, 60]
'''
