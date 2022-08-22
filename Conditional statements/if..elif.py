# calculate student average marks and assign a grade value
tel = 88
eng = 55
maths = 50
science = 55
social = 78
hindi = 35

avg = (tel+eng+maths+science+social+hindi)/6
if avg>90:
    grade = "A+"
elif avg>80:
    grade = "A"
elif avg>70:
    grade = "B+"
elif avg>60:
    grade = "B"
elif avg>50:
    grade = "C+"
elif avg>40:
    grade = "C"
elif avg>34:
    grade = "Pass"
else:
    grade = "Fail"

print("have you grade is {}".format(grade))