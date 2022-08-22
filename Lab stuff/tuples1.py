# tuple is a read only list.
# tuples are immutable

marks=(96,87,67,81,81)
print(type(marks))
print(len(marks))
print(sum(marks))
print(min(marks))
print(max(marks))
print(sum(marks)/len(marks))

# operations
print((3,4,5) + (2,7,8))
print((1,2,3) * 5)

# indexing

print(marks[0])
print(marks[-1])

# slicing

print(marks[2:5])

print(sum(marks[-3:]))  # sum of last 3 elements


# tuple methods

friends = 'hari','sita','giri','gita'


print(type(friends))
# query

print(friends.index('hari'))
print(friends.count('hari'))


# iterating a list

for friend in friends:
	print(friend)

for friend in friends:
	print(friend.upper())

for index, friend in enumerate(friends):
	print(index, friend)

for index, friend in enumerate(friends):
	print("{} is at index {}".format(friend.capitalize(), index))