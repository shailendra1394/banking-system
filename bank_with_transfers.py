from datetime import timedelta, datetime

from bank import Bank
from transfer import Transfer


class BankWithTransfers(Bank):
    def __init__(self):
        super().__init__()
        self.transfers = []

    def schedule_transfer(self, from_account_id, to_account_id, amount, time_delay):

        if from_account_id in self.accounts and to_account_id in self.accounts:
            from_account = self.accounts[from_account_id]
            to_account = self.accounts[to_account_id]
            scheduled_time = datetime.now() + timedelta(seconds=time_delay)

            transfer = Transfer(from_account, to_account, amount, scheduled_time)

            self.transfers.append(transfer)

        else:
            print("Invalid IDs!!!")

    def check_transfer_status(self):

        for transfer in self.transfers:
            transfer.execute_transfer()
            print(f"Transfer from Acc of {transfer.from_account.owner_name}"
                  f" to Acc of {transfer.to_account.owner_name}"
                  f" for the amount of {transfer.amount}"
                  f" is {transfer.status}.")
