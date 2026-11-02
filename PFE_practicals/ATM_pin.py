def pin_sys():

    while True:
        
        pin=int(input("Enter the pin:"))
        if pin==1234:
            print("PIN Verified.")

            return 1
        
        else:
            print("Incorrect PIN , enter the correct PIN!!")

