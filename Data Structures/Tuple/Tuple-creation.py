# Diff types of creation tuple

tup1 = ('Aharonu')
print(type(tup1))
# <class 'str'>
tup2 = ('Aharonu',)
print(type(tup2))
# <class 'tuple'>

tup3 = tuple('Aharonu')
print(tup3)
# ('A', 'h', 'a', 'r', 'o', 'n', 'u')
tup4 = tuple(range(1,10))
print(tup4)
# (1,2, 3, 4, 5, 6, 7, 8, 9)

mix_tup = ("N",7,"I",1,56)
for i in mix_tup:
  print(i)