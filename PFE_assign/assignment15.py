#PROGRAM TO FIND THE ROOTS OF QUADRATIC EQUATION
import math

a=float(input("Enter the coefficient of x^2 :"))
b=float(input("Enter the coefficient of x :"))
c=float(input("Enter the constant :"))

if (((b**2)-4*a*c)>=0):

    x1=(-b+math.sqrt((b**2)-4*a*c))/(2*a)
    x2=(-b-math.sqrt((b**2)-4*a*c))/(2*a)

    print(f"The roots of equation are {x1},{x2}.")

else:
    print("The equation doesn\'t have real roots.")

