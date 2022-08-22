# list methods

friends = ['hari','sita','giri','gita']

# adding elements

print(friends)
friends.append('siri')
print(friends)
friends.insert(1,'sri')
print(friends)
# remove elements

friends.remove('sri')
print(friends)
friends.pop(2)
print(friends)

# sort

friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

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