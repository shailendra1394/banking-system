from bank_account import BankAccount


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, owner_name):
        self.accounts[account_id] = BankAccount(account_id, owner_name)

    def delete_account(self, account_id):
        del self.accounts[account_id]

    def rank_accounts(self):
        ranked_acc = sorted(self.accounts.values(), key=lambda x: sum(sum(t.values()) for t in x.transactions), reverse=True)
        for rank, account in enumerate(ranked_acc, start=1):
            print(
                f"Rank {rank}: {account.owner_name} with total transaction value {sum(sum(t.values()) for t in account.transactions)}")
