t=int(input("Enter the tenperature :"))

if t<0:
    print("It,s freezing temperature.")
elif 0<t<30:
    print("Its,s normal temperature.")
elif 31<t<60:
    print("Warning temperature.")
elif t>60:
    print("Very high temperature.")
else:
    print("Enter a vlaid choice.")