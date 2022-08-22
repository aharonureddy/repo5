# it return a reverse iterator object. Seq must be an object

tup1 = (4,2,10,6)
print(reversed(tup1))  # it return a object
'''
<reversed object at 0x000001E88D0165C0>
'''
print(tuple(reversed(tup1)))    # (6, 10, 2, 4)

tup2 = ('nit','Aharonu','Python')
print(tuple(reversed(tup2)))   # ('Python', 'Aharonu', 'nit')

tup3 = ('1','121','484')
print(tuple(reversed(tup3)))    # ('484', '121', '1')

tup4 = (1,121,484)
# print(tuple(reversed(tup4[1])))  TypeError: 'int' object is not reversible



