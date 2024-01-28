from infrastructure_layer import AccountRepository
from usecase_layer import CreateAccountUseCase, TransactionUseCase, AccountStatementUseCase

# Simple test scenario
if __name__ == "__main__":
    account_repo = AccountRepository()
    create_account_use_case = CreateAccountUseCase()
    transaction_use_case = TransactionUseCase()

    # Creating a new account
    new_account = create_account_use_case.create_account(
        customer_id="123",
        name="Prasad",
        email="prasad@example.com",
        phone_number="1234567890"
    )

    account_repo.save_account(new_account)

    # Making a deposit
    transaction_use_case.make_transaction(new_account, amount=1000, transaction_type='deposit')

    # Making a withdrawal
    transaction_use_case.make_transaction(new_account, amount=500, transaction_type='withdraw')

    # Generating account statement
    account_statement_use_case = AccountStatementUseCase()
    statement = account_statement_use_case.generate_account_statement(new_account)

    print(f"Account Balance: {new_account.get_balance()}")
    print("Account Statement:")
    print(statement)
