lst1 = ['nit', 'Aharonu IT', 45,67]
print('nit' in lst1)    # true

lst2 = ['NIT', 'Aharonu IT', 45,67]
print(lst1 in lst2)      # false

# example: To find list of elements to equal and store in another list
print("----------------------")
lst1 = ['nit', 'Aharonu IT', 45,67]
lst2 = ['NIT', 'Aharonu IT', 45,67]
lst3=[0]
idx=-1
equal = 0
'''Create list index with zero (0) elements'''
for i in lst1:
    idx+=1
    if i==lst2[idx]:
        equal+=1
lst3=lst3*equal
idx=-1
n=0
'''storing values list values '''
for i in lst1:
    idx+=1
    if i==lst2[idx]:
        lst3[n]=i
        n+=1
print(lst3)



