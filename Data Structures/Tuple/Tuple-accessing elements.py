'''To access data items of a tuple we use following ways
indexing a tuple
iteration using loops
slicing of tuple'''

# indexing a tuple
tup1 = ('nit',10,20,30,40,'Aharonu IT')
print(tup1[0])     # nit
print(tup1[2])    # 20
print(tup1[len(tup1)-1])    # Aharonu IT

# we have to creare tuple with data items a l ist, tuple and number
tup = (1,(2,3,4),[5,6,7])
print(tup[0])    # 1
print(tup[1])    # (2,3,4)


# Iteration using loops:
# using for loop
product = (1,("samsung","lenovo","hp"),['windows 7','linux','ubunt'])
for i in product:
    print(i)
'''
1
('samsung', 'lenovo', 'hp')
['windows 7', 'linux', 'ubunt']
'''

# using  while loop
tup2 = (10,20,30,40,50)
i=0
while i < len(tup2):
    print(tup2[i])
    i+=1

'''
10
20
30
40
50
'''

# Accessing elements using slicing operator
tup3 = ("nit","coures","projects","batches","contact")
print(tup3[2:])            # ('projects', 'batches', 'contact')
print(tup3[:])            # ('nit', 'coures', 'projects', 'batches', 'contact')
print(tup3[::])           # ('nit', 'coures', 'projects', 'batches', 'contact')
print(tup3[:3])           # ('nit', 'coures', 'projects')
print(tup3[2:5])          # ('projects', 'batches', 'contact')
print(tup3[:-1])          # ('nit', 'coures', 'projects', 'batches')
print(tup3[-1:])          # ('contact',)
print(tup3[1:5:2])        # ('coures', 'batches')
print(tup3[-5:None:-1])   # ('nit',)
print(tup3[5:0:-1])       # ('contact', 'batches', 'projects', 'coures')
print(tup3[2:None:-1])    # ('projects', 'coures', 'nit')


# example, tuple assign elements through slice operators
tup3 = ("nit","coures","projects","batches","contact")
tup4 = ("Aharonu IT",)
tup4+=tup3[:]
print(tup4)
# ('Aharonu IT', 'nit', 'coures', 'projects', 'batches', 'contact')

tup5 = tup4[0:None:2]
print(tup5)
# ('Aharonu IT', 'coures', 'batches')