from domain_layer import Account, Customer
from utility import generate_account_id, generate_account_number

# Use Case layer
class CreateAccountUseCase:
    def create_account(self, customer_id, name, email, phone_number):
        account_id = generate_account_id()  
        account_number = generate_account_number()
        account = Account(account_id, customer_id, account_number)
        customer = Customer(customer_id, name, email, phone_number)
        # Perform any additional operations related to creating an account
        return account


class TransactionUseCase:
    def make_transaction(self, account, amount, transaction_type):
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")


class AccountStatementUseCase:
    def generate_account_statement(self, account):
        statement = f"Account Statement for Account ID {account.account_id}\n"
        statement += f"Account Number: {account.account_number}\n"
        statement += f"Customer ID: {account.customer_id}\n"
        statement += f"Current Balance: {account.get_balance()}\n\n"
        statement += "Transactions:\n"

        for transaction in account.transactions:
            statement += f"{transaction['timestamp']} - {transaction['type'].capitalize()}: {transaction['amount']}\n"

        return statement
