#Hans
#ATM
#Tracks money and how much you have it in your bank account

balance = 100
def deposit(amount):
    global balance
    balance = balance + amount
    print("deposited", amount)
def withdraw(amount):
    global balance
    balance = balance - amount
    print("withdrew", amount)
def total():
    global balance
    print(balance)
deposit(40)
withdraw(20)
total()
