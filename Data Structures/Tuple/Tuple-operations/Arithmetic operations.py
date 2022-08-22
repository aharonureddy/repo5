# Tuple only can perform addition and multiplication

tup1 = (1,2,3,4,5)
tup2 = (6,7,8,9,10)
tup3 = tup1 + tup2
print(tup3)
# output: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# exmaple  - addiiton
tup1 = (1,2,3,4,5)
tup2 = (6,7,8,9,10)
print(tup1)
print(tup2)
tup4=()
j=0
for i in range(len(tup1)):
    j=tup1[i] + tup2[i]
    tup4+=(j,)
print("after assign values is  : ")
print(tup4)
'''output:
(1, 2, 3, 4, 5)
(6, 7, 8, 9, 10)
after assign values is  : 
(7, 9, 11, 13, 15)
'''

# exmaple  - multiplication
tup5 = (1,2,3,4,5)
print("before modify data tuple is ")
print(tup1)
tup6=()
j=0
for i in tup5:
    j=i*5
    tup6+=(j,)
tup5=tup6
print("after modify data tuple is tup5*5 ")
print(tup5)
'''
output:
after assign values is  : 
(7, 9, 11, 13, 15)
before modify data tuple is 
(1, 2, 3, 4, 5)
after modify data tuple is tup5*5 
(5, 10, 15, 20, 25)
'''