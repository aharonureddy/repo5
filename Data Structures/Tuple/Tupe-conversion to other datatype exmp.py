tup1 = ('nit',2,4,3,2,4,'nit')
print(tup1)

list1 = list(tup1)
print(type(list1))
print(list1)  # <class 'list'>  ['nit', 2, 4, 3, 2, 4, 'nit']

set1 = set(tup1)
print(type(set1))
print(set1)   # <class 'set'>  {2, 3, 4, 'nit'}

str1 = str(tup1)
print(type(str1))
print(str1)     # <class 'str'>  ('nit', 2, 4, 3, 2, 4, 'nit')

tup2 = (1,(1,2),[1,2,3],2,3)
print(tup2)   # (1, (1, 2), [1, 2, 3], 2, 3)

list2 = list(tup2)
print(list2)    # [1, (1, 2), [1, 2, 3], 2, 3]

str2 = str(tup2)
print(str2)   # (1, (1, 2), [1, 2, 3], 2, 3)

# note: nested tuple elements can not coveret to set

set2 = set(tup2)
print(set2)   # TypeError: unhashable type: 'list'