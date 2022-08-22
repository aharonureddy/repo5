# it return a new sorted list from the items in iterable. Here function takes two keyword arguments

num_list = ['45','134','233','4','7']
print(num_list)
print(sorted(num_list))
# ['134', '233', '4', '45', '7']

print(sorted(num_list,key=int))
# ['4', '7', '45', '134', '233']

print(sorted(num_list,key=int,reverse=True))
# ['233', '134', '45', '7', '4']

print(num_list)
# ['45', '134', '233', '4', '7']


