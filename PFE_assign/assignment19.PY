#DIFFERENCE IN SECONDS BETWEEN TWO TIMESTAMP 

H1=int(input("Enter the number of hours in first timestamp :"))
M1=int(input("Enter the number of minutes in first timestamp :"))
S1=int(input("Enter the number of seconds in first timestamp :"))
H2=int(input("Enter the number of hours in second timestamp :"))
M2=int(input("Enter the number of minutes in second timestamp :"))
S2=int(input("Enter the number of seconds in second timestamp :"))

print(f"The difference between the timestamp in seconds is {abs(((H1*3600)+(M1*60)+S1)-((H2*3600)+(M2*60)+S2))}")