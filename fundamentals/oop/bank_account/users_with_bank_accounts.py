
class BankAccount:
    bank_account_list = []

    def __init__(self, int_rate=1, balance=0): 
        self.int_rate = int_rate/100
        self.balance = balance

        BankAccount.bank_account_list.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance: $", self.balance) 
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.bank_account_list:
            print(f"Interest Rate: {account.int_rate}, Balance: ${account.balance}")

        return BankAccount.bank_account_list


class User:
# Update the User class __init__ method
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

# Update the User class make_deposit method
    def make_deposit(self, amount):	
        self.account.balance += amount
        self.display_user_balance()	
        return self

# Update the User class make_withdrawal method
    def make_withdrawl(self, amount): 
        self.account.balance -= amount
        return self

# Update the User class display_user_balance method
    def display_user_balance(self): 
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

# Update the User class transfer_money method
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.make_deposit(amount)

        print(f"User: {self.name}, Balance: ${self.account.balance}")
        print(f"User: {other_user.name}, Balance: ${other_user.account.balance}")
        return self


deidre = User("Deidre La Couse", "DeLaCouse@airs.com", BankAccount())
print(deidre.account.int_rate)

deidre.make_deposit(100).make_withdrawl(50).display_user_balance()

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to