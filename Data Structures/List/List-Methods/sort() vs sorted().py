'''
List.sort(): it is nothing return but it modified original list
sorted():  it returns a list with sorted elements but not modified original list
reversed(seq) : return a reverse iterator object. Seq must be an object
'''


num_list = ['45','134','233','4','7']
print(num_list)
print(reversed(num_list))
print(num_list)

lst1=list(reversed(num_list))
print(lst1)

'''
['45', '134', '233', '4', '7']
<list_reverseiterator object at 0x0000021CD4F75390>
['45', '134', '233', '4', '7']
['7', '4', '233', '134', '45']
'''

num_list = ['45','134','233','4','7']
lst2 = list(reversed(sorted(num_list,key=int)))
print(lst2)
# ['233', '134', '45', '7', '4']

