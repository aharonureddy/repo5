tup1 = (("Ammerpet","Hyderabad"),'+91 9989553009','aharonu05@gmail.com')
address,Tel,Email = tup1
print(address)
# ('Ammerpet', 'Hyderabad')


# Assign element into tuple
tup2 = ('cources',['python','Django','Data Sciens'],
        "database",['mysql','oracle','sql server','sqlite'])
print(tup2[1])   # ['python', 'Django', 'Data Sciens']

tup2[1][2] = 'IOT'
print(tup2[1])   # ['python', 'Django', 'IOT]

# note: explanation : we can assign tuple elements within list


# the following example to swap a variables single elements
a,b = 57,65
print(a,b)    # 57 65
(a,b) = (b,a)
print(a,b)    # 65 57

# note: we can not directly assign an item because tuple an immutabel data type i.e you can not modify the elements.
tup3 =(10,(20,30),[40,50,60])
print(tup3[2])     # [40, 50, 60]
tup3[2][2] = 70
print(tup3[2])     # [40, 50, 70]


# can not and can example tuple
tup4 = ('Ammerpet','Hyderabads')
print(tup4)
# tup4[2]=('aharonu05@gamil.com')
    # TypeError: 'tuple' object does not support item assignment


# we can concatenate tuple with addition + operator as follows
tup5 = ('Ammerpet','Hyderabads')
tup5=tup5+("aharonu05@gamil.com",)
print(tup5)   # ('Ammerpet', 'Hyderabads', 'aharonu05@gamil.com')


# following example we can list data into a tuple
lst_courses = ["python","django", "java"]
tup6 = ('nit',)
tup6+=(lst_courses,)
print(tup6)       # ('nit', ['python', 'django', 'java'])


