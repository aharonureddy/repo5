# how to execute else body part
avg = 33
if avg > 60:
    grade = "First Class"
elif avg > 50:
    grade = "Second Class"
elif avg > 36:
    grade = "third class"
else:
    grade = "Fail"
print("you are a {}".format(grade))