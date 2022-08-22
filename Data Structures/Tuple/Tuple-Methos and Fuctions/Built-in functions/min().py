# it returns smallest item in the sequence. It compare element through ascil value

tup1 = ('nit','courses','projects','batches','contact')
print(min(tup1))    # batches

tup2 = (34,12,56,78)
print(min(tup2))   # 12

tup4 = ((1,),(1,2),(1,2,3))
print(min(tup4))    # (1,)

tup5 = ((1,2),(2,1),(1,3))
print(min(tup5))   # (1,2)


nest_tup1 = ((1,'d'),(3,'a'),(-1,'b'),(2,'c'))
print(min(nest_tup1))   # (-1, 'b')

tup3 = (12,(45,2),[34,45])
print(min(tup3))     # TypeError: '<' not supported between instances of 'tuple' and 'int'