# sets

a = {2,5,3,5,6,4,5,3,4,234}
b = {3,5,8}

print(type(a))
print(a)

print(b)
b.add(40)
b.add(3)
print(b)

x = {1,2,3,4}
y = {3,4,5,6}

print(x.union(y))
print(x.intersection(y))

data = [1,2,3,4,5,3,4,5,6,2,3,4,5,6,7,4,5,6]

unique = set(data) # duplicate removal

print(unique)




