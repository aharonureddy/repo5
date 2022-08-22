# The index method searches for the given itemin the list and return its index position. If the given item is present more
# than one then index position of the first occurance returned

lst1 = [10,20,30,10,20,30,10,20,30]
print(lst1.index(30))    # return 30 value first index 2

print(lst1.index(20,2,7))    # search from 2nd index to 7th index in list return 20 value index 4
print(lst1.index(10,1))      # search from 1st index return 10 value index first occurence 3

# negative index based
print(lst1.index(10,-5))     # search from last five element and return positive index value of 10 is 6
print(lst1.index(10,-8,-4))  # return positive index value of 10 between -8th index and -4th index range 3


x=["Python", "Datascience", "Hadoop"]
print(x.index('Hadoop'))   # 2

print(lst1.index(10,-(len(lst1)) + 1))  # 3
print(lst1.index(10,1))  # 3

print(lst1.index(10,round(len(lst1)/2)))  # search from middle list 6