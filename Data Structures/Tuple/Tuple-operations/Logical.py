
tup1 = (1,2,3,4,5)
tup2 = (6,7,8,9,10)
print(tup1 and tup2)   # (6, 7, 8, 9, 10)
print(tup1 or tup2)    # (1, 2, 3, 4, 5)

tup3 = (0,1)
tup4 = (1,0)
print(tup3 and tup4)   # (1,0)
print(tup3 or tup4)    # (0,1)

tup5 = (0,1)
tup6 = (0,1)
print(tup5 & tup6)
# TypeError: unsupported operand type(s) for &: 'tuple' and 'tuple'
