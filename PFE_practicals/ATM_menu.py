import ATM_pin

print("1 Balance 2 Withdraw 3 Deposit 4 Exit")
balance=50000

while True:
    n=int(input("Enter your choice:"))

    if n==1:
        passing=ATM_pin.pin_sys()
        if passing==1:
            print(f"Your balance is {balance}")

    elif n==2:
        passing=ATM_pin.pin_sys()
        if passing==1:
            withdraw=int(input("Enter withdrawl amount:"))
            balance-=withdraw
            print(f"Your current balance is ₹{balance}")

    elif n==3:
        passing=ATM_pin.pin_sys()
        if passing==1:
            deposit=int(input("Enter the amount to deposit:"))
            balance+=deposit
            print(f"Your current balance is ₹{balance}")

    elif n==4:
        print("You have exited the menu.")
        break
        

