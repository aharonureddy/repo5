# it returns the largest element in the iterabel or the largest of two or more arguments

tup_num = ('45','34','134','44','233','4','7')
print(max(tup_num))    # 7

print(max(tup_num,key=int))   # 233

tup1 = ((1,),(1,2),(1,2,3))
print(max(tup1))     # (1,2,3)

tup2 = ((1,),(10,20),(1,2))
print(max(tup2))    # (10,20)
