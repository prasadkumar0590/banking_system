from datetime import datetime

# Domain layer
class Account:
    def __init__(self, account_id, customer_id, account_number, balance=0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance
        self.transactions = []  # Store transactions for the account

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({"type": "deposit", "amount": amount, "timestamp": datetime.now()})

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append({"type": "withdraw", "amount": amount, "timestamp": datetime.now()})
        else:
            raise ValueError("Insufficient funds")

    def get_balance(self):
        return self.balance

class Customer:
    def __init__(self, customer_id, name, email, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number