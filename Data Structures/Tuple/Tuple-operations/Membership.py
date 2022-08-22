# membership operator
# the following example to compare the elements
tup1 = ("nit","Aharonu IT","Hello",34,25)
print("nit" in tup1)     # true

tup2 = ("nit","ncare","NIT",33,25)
print(tup1 in tup2)      # false

# example print common elements
tup1 = ("nit","Aharonu IT","Hello",34,25)
tup2 = ("nit","ncare","NIT",33,25,"Hello")
tup3 = ()
for i in tup1:
    if i in tup2:
        tup3+=(i,)
print(tup3)
# ('nit', 'Hello', 25)