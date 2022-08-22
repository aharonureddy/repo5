# a nested list is a list that appears as an element in another list. It is like a tow dimensional array
# syntax: list1 = [ [..],[..],[,,] etc. ]
# example, creation a nested list
list1 = [[10,20,30],
         [40,50,60],
         [70,80,90]
         ]
print(list1)
# [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

print(list1[0][1])   # 20
print(list1[-3][-2])   # 20
print(list1[1][1])  # 50


# we can change to the nested list values
list1[-1][1] = 85
print(list1)
# [[10, 20, 30], [40, 50, 60], [70, 85, 90]]
