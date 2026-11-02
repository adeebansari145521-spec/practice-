a1=float(input("Enter the angle of triangle:"))
a2=float(input("Enter the angle of triangle:"))
a3=float(input("Enter the angle of triangle:"))

if (a1+a2+a3)==180:
    print("The triangle is valid.")
elif a1<0 or a2<0 or a3<0:
    print("The triangle is invalid.")

if a1<90 and a2<90 and a3<90 :
    print("The triangle is acute.")
elif a1>90 or a2>90 or a3>90 :
    print("The triangle is obtuse.")
else:
    print("The triangle is right angled.")



