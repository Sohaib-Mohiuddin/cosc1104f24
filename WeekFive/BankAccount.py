'''
Problem:
Create a BankAccount class that simulates a simple bank account. The class should have the following:

Attributes:
    account_holder: The name of the account holder.
    balance: The balance of the account (initially 0).

Methods:
    deposit(amount): Adds the given amount to the balance.
    withdraw(amount): Deducts the given amount from the balance if there are sufficient funds, otherwise prints an error message.
    display_balance(): Prints the current balance.

Create an instance of the BankAccount class for a user, make a few deposits and withdrawals, and display the final balance.
'''

class BankAccount:
    # Constructor / Initialization of Class
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    # Method to Deposit Money
    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
            print(f"Successfully Deposited ${ amount } into { self.account_holder }'s Account.")
            self.display_balance()
        else:
            print(f"${ amount } is not an acceptable amount.")
    
    # Method to Withdraw Money
    def withdraw(self, amount):
        if (amount > 0):
            if (amount <= self.balance):
                self.balance -= amount
                print(f"Successfully Withdrawn ${ amount } from { self.account_holder }'s Account.")
                self.display_balance()
            else:
                print(f"Insufficient Funds in { self.account_holder }'s Account.")
        else:
            print(f"${ amount } is not an acceptable amount.")
    
    # Method to Display Balance
    def display_balance(self):
        print(f"Current Balance for { self.account_holder }: ${ self.balance }")
