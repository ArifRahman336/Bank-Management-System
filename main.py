from register import *
from bank import *
print('Welcome to Arif Banking Project')
status = False
while True:
    try:
        print("\nChoice Option: ")
        print("1.SignUp")
        print("2.SignIn")
        register = int(input("Select One Option: "))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                status = True
                break
        else:
            print('Please Enter Valid Input From Options')
    except ValueError:
        print("Invalid Input Try Again with Numbers")


account_number = db_query(f"select account_number from customers where username = '{user}';")


while status:
    try:
        # print("\nChoice Option: ")
        print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
        print("1.Balance Enquiry")
        print("2.Cash Deposit")
        print("3.Cash WithDraw")
        print("4.Fund Transfer")
        facility = int(input("Select One Option: "))
        if facility >= 1 and facility <= 4:
            if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.balanceequiry()
            elif facility == 2:
                 while True:
                    try:
                        amount = int(input("Enter Amount to Deposit"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
                
            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
                
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number"))
                        amount = int(input("Enter Money to Transfer"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue

        else:
            print('Please Enter Valid Input From Options')
            continue
    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue