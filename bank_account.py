class BankAccount:

    def __init__(self, account_id, owner_name):

        self.account_id = account_id
        self.owner_name = owner_name

        self.transactions = []
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({"Deposit:": amount})

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append({"Withdrawal:": amount})
        else:
            print("Insufficient Funds!")

