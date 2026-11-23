
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance

    def check_balance(self):
        print("\n----- BANK ACCOUNT DETAILS -----")
        print("Account Holder:", self.name)
        print("Account Number:", self.acc_num)
        print("Available Balance: ₹", self.balance)


# Create a bank account
account = BankAccount(
    "Ashwini",
    "1234567890",
    30000
)

# Check bank balance
account.check_balance()
