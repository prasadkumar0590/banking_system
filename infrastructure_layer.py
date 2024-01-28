# Infrastructure layer
class AccountRepository:
    accounts = []

    def save_account(self, account):
        self.accounts.append(account)

    def find_account_by_id(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def find_accounts_by_customer_id(self, customer_id):
        return [account for account in self.accounts if account.customer_id == customer_id]
