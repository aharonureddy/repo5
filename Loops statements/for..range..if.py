#example:  list items find the negative numbers and displayed

x = [3,6,-5,-4,3,-5,-4]

for i in range(len(x)):
   if x[i] < 0:
      print("found a negative number at position ", i)

