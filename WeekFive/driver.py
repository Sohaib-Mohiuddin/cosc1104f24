from BankAccount import *

if __name__ == "__main__":
    sohaib = BankAccount('Sohaib')
    sohaib.deposit(20)
    sohaib.deposit(40)
    sohaib.withdraw(100)
    sohaib.deposit(70)
    sohaib.deposit(10)
    sohaib.withdraw(20)
    sohaib.deposit(20)
    
    mihir = BankAccount('Mihir')
    mihir.deposit(200)
    mihir.deposit(3000)
    mihir.withdraw(2000)
    mihir.deposit(1)