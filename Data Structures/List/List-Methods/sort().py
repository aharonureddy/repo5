
lst1 = [12,34,89,9,11,11]
lst1.sort()
print(lst1)
# output: [9, 11, 11, 12, 34, 89]

lst2 = [12,34,89,9,11,11]
lst2.sort(reverse=True)
print(lst2)
# output : [89, 34, 12, 11, 11, 9]

lst3 = ["abc","acb","abca","abcd"]
lst3.sort()
print(lst3)
# ['abc', 'abca', 'abcd', 'acb']

lst4 = ["abc","acb","abca","abcd"]
lst4.sort(key=len)
print(lst4)
# ['abc', 'acb', 'abca', 'abcd']

lst4.sort(key=len,reverse=True)
print(lst4)
# ['abca', 'abcd', 'abc', 'acb']


num_list = ['34','34','134','44','233','4','7']
num_list.sort()
print(num_list)
# ['134', '233', '34', '34', '4', '44', '7']

num_list = ['34','34','134','44','233','4','7']
num_list.sort(key=int,reverse=True)
print(num_list)
# ['233', '134', '44', '34', '34', '7', '4']

