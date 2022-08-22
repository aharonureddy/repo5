# 2. Accept the three angles of a triangle and print if it is an isosceles triangle or not

angle1 = int(input("Enter angle 1 :"))
angle2 = int(input("Enter angle 2 :"))
angle3 = int(input("Enter angle 3 :'))


if angle1==angle2 or angle2==angle3 or angle1==angle3:
    print("isosceles triangle")
else:
    print("non-isosceles triangle")
    
