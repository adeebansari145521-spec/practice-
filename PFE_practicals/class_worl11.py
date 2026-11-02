l=int(input("Enter the water level in percentage :"))

litre= 10*l
print(f"{litre} litre of water is filled in the tank and {1000-litre} is still empty.")

if l<20:
    print("The water level is low in the tank. ")
elif 20<l<80:
    print("Water level is normal in the tank.")
elif 80<l<100:
    print("Water level is high in the tank.")
else:
    print("Enter a valid percentage")