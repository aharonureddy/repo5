# return the largest element in the iterable or the largest of two or more arguments

num_list = ['34','34','134','44','233','4','7']
print(max(num_list))   # 7
print(max(num_list,key=int))   # 233

lst1=[0.5,45,45.5,5,3.4]
print(max(lst1,key=int))   # 45


# min: return the smallest element in the iterable or the smallest of two or more arguments
lst2 = [34,23,11,15]
print(min(lst2))    # 11

lst3 = ['abc','abd','aac','bbc']
print(min(lst3))    # aac
