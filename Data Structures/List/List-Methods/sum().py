'''Sums start and the items of an iterable form left to right and returns the total
The iterable's items are normally numbers, and the start value is not allowed to be a string
start defaults to 0'''

num_list = [45,134,233,4,7]
print(sum(num_list))   # 423
print(sum(num_list,10)) # 433

# the following example string numerical values sum by using generator expression
num_list1 = ['45','134','233','4','7']
tot_list = sum(int(i) for i in num_list1)     # generator expression
print(tot_list)      # 423

tot_list = sum((int(i) for i in num_list1),10)
print(tot_list)       # 433

