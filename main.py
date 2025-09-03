import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    # Load existing data (if file exists)
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("File not found, creating new database.")
    except Exception as err:
        print(f"Error occurred: {err}")

    @classmethod
    def update(cls):
        """Save current data to JSON file"""
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def deposit(cls, account_no, amount):
        """Deposit money into an account"""
        for i in cls.data:
            if i["account_no"] == account_no:
                i["balance"] += amount
                print(" Your account has been updated")
                cls.update()
                break
        else:
            print(" Account not found")

    @classmethod
    def withdraw(cls, account_no, amount):
        """Withdraw money from an account"""
        for i in cls.data:
            if i["account_no"] == account_no:
                if i["balance"] >= amount:
                    i["balance"] -= amount
                    print("Withdrawal successful")
                    cls.update()
                else:
                    print(" Insufficient balance")
                break
        else:
            print(" Account not found")

    @classmethod
    def show_details(cls, account_no):
        """Show account details"""
        for i in cls.data:
            if i["account_no"] == account_no:
                print(json.dumps(i, indent=4))
                break
        else:
            print("Account not found")

    def create_account(self):
        """Create a new account"""
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your 4-digit PIN: ")),
            "account_no": random.randint(1000, 9999),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print(" You are not eligible for creating an account")
        else:
            print(" Account created successfully!")
            for k, v in info.items():
                print(f"{k}: {v}")
            print(" Your account number is:", info["account_no"])

            Bank.data.append(info)
            Bank.update()


# ----------- Menu System ------------
user = Bank()
print(" Welcome to the Bank")
while True:
    print("\nChoose an option:")
    print("1. Create an account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Show account details")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user.create_account()
    elif choice == "2":
        acc = int(input("Enter account number: "))
        amt = int(input("Enter deposit amount: "))
        Bank.deposit(acc, amt)
    elif choice == "3":
        acc = int(input("Enter account number: "))
        amt = int(input("Enter withdrawal amount: "))
        Bank.withdraw(acc, amt)
    elif choice == "4":
        acc = int(input("Enter account number: "))
        Bank.show_details(acc)
    elif choice == "5":
        print("Thank you for banking with us!")
        break
    else:
        print(" Invalid choice")
