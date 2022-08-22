# example: calculate the total marks and pass or fail

lst = [88,54,67,36,34]
k=0
total=0
for i in lst:
    if i < 35:
        k=1
        break
    total = total+i
if k==1:
    print("Fail")
else:
    print("Pass total marks is : ", total)
