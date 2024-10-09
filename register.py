# User Registration Signin Signup
from database import *
from customer import *
from bank import Bank
import random
def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"select username from customers where username = '{username}';")
    if temp:
        print('Username Already Exists')
        SignUp()
    else:
        print('Username is Available Please Proceed')
        password = input('Enter Your Password: ')
        name = input('Enter Your Name: ')
        age = input('Enter Your Age: ')
        city = input('Enter Your City: ')
        while True:
            account_number = int(random.randint(100000000, 999999999))
            temp = db_query(f"select account_number from customers where account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number: ",account_number)
                break
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username,account_number)
    bobj.create_transaction_table()

def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"select username from customers where username = '{username}';")
    if temp:
        while True:
            account_number = int(input(f"Welcome {username.capitalize()} Enter Account Number: "))
            temp = db_query(f"select account_number from customers where username = '{username}';")
            print(temp[0][0])
            if temp[0][0] == account_number:
                print("Sign In Succesfully !")
                return username
            else:
                print("Wrong account number Try Again")
    else:
        print("Enter Correct Username")
        SignIn()