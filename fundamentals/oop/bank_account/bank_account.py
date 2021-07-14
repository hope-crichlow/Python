class BankAccount:
# A list to hold all instances of BankAccount  
    bank_account_list = []

# The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. 
    def __init__(self, int_rate=1, balance=0): 
        self.int_rate = int_rate/100
        self.balance = balance

        BankAccount.bank_account_list.append(self)

# Increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount

        # self.display_account_info()
        return self

# Decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

        # self.display_account_info()
        return self

# Print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print("Balance: $", self.balance)
        
        return self

# Increases the account balance by the current balance * the interest rate (as long as the balance is positive)  
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)

            # self.display_account_info()
            return self

# Use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def display_all_accounts(cls):
        for account in cls.bank_account_list:
            print(f"Interest Rate: {account.int_rate}, Balance: ${account.balance}")

        return BankAccount.bank_account_list


# Create 2 accounts
checking = BankAccount()
savings = BankAccount(2.3, 75)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
checking.deposit(50).deposit(500).deposit(65).withdraw(20).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
savings.deposit(75).deposit(400).withdraw(60).withdraw(500).withdraw(20).withdraw(100).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.display_all_accounts()