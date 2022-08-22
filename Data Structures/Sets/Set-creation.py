set1 = set()
print(set1)

set2 = {}
print(set2)
print(type(set2))

s1 = set('Aharonu')
print(s1)

s2 = set({10,20,30,30,30})   # set argument
print(s2)

s3 = set([10,20,30,30,20])   # list argument
print(s3)

'''output:
set()
{}
<class 'dict'>
{'u', 'h', 'A', 'a', 'r', 'o', 'n'}
{10, 20, 30}
{10, 20, 30}
'''

mix_set= {10,'Aharonu',4.5,(2,4)}    # tuple inside set
for i in mix_set:
  print(i)

'''
Aharonu
10
4.5
(2, 4)
'''

# note: we can not store a nested list in a set but we can store a tuple
# list - set example
list1 = [10,20,[20,30]]
s1 = set(list1)
print(list1)

'''
    s1 = set(list1)
TypeError: unhashable type: 'list'
'''
mix_set2 = {10,'Aharonu',4.5,[2,4]}  # list inside set
for i in mix_set:
  print(i)

# TypeError: unhashable type: 'list'.


# tuple - set example
tup1 = (10,20,(10,20))
s4 = {tup1}
print(s4)
for i in s4:
    print(s4,'-->',type(s4))
# the above example it createdd whole data in single tuple but we need different data type's creation with single arguments
tup1 = (10,20,(10,20))
s4 = set(tup1)
print(s4)
for i in s4:
    print(s4,'-->',type(s4))
