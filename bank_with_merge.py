from bank_with_transfers import BankWithTransfers


class BankWithMerge(BankWithTransfers):
    def merge_accounts(self, account_id_1, account_id_2):
        if account_id_1 in self.accounts and account_id_2 in self.accounts:
            account_1 = self.accounts[account_id_1]
            account_2 = self.accounts[account_id_2]

            account_1.balance += account_2.balance
            account_1.transactions.extend(account_2.transactions)

            self.delete_account(account_id_2)

        else:
            print("Invalid IDs!!!")


bank = BankWithMerge()

bank.create_account(5345350, "Ram")
bank.create_account(5345351, "Shyam")
bank.create_account(5345352, "Bharat")

bank.accounts[5345350].deposit(1000)
bank.accounts[5345351].deposit(700)
bank.accounts[5345352].deposit(500)

bank.accounts[5345352].withdrawal(300)
bank.accounts[5345351].withdrawal(300)
bank.accounts[5345350].withdrawal(300)


bank.rank_accounts()
print("-----------------------------------------")

bank.schedule_transfer(5345350,5345352,100,0)

bank.check_transfer_status()