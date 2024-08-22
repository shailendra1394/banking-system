from datetime import datetime


class Transfer:
    def __init__(self, from_account, to_account, amount, scheduled_time):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.scheduled_time = scheduled_time

        self.status = "Scheduled"

    def execute_transfer(self):
        if self.scheduled_time <= datetime.now():
            if self.from_account.balance >= self.amount:
                self.from_account.balance -= self.amount
                self.to_account.balance += self.amount

                self.status = "Completed"

            else:
                self.status = "Insufficient Funds!!"

        else:
            print("Scheduled for future.")
