# The comparison operator starts with a first element of each tuple. Don't compare to < or > or = or first element then it proceed
# wot the second element and so on.

tup1 = (1,2,3,4)
tup2 = (4,2,10,6)
print(tup1 == tup2)   # 1==4 ; False
print(tup1 >  tup2)   # 1>4 ; False
print(tup1 <= tup2)   # 1<=4 ; True
# note: here, tup1 > tup2 is compare first element condtion is true then it is not going ot next element


tup3 = (1,2,3)
tup4 = (1,2,4)
print(tup3 < tup4 )  # 1<1, 2<2, 3<4 ; True
print(tup3 > tup4 )  # False
print(tup3 <= tup4 )  # True
print(tup3 != tup4 )  # 1!=1, 2!=2, 3!=4 ; True

# exmaple, in above list
tup3 = (1,2,3)
tup4 = (1,2,4)
equal = 0
notequal = 0
for i in range(len(tup3)):
    if tup3[i] == tup4[i]:
        equal+=1  # equal = equal + 1
    else:
        notequal+=1
print("Total equal numbers is : ", equal)
print("Total not equal numbers is : ",notequal)