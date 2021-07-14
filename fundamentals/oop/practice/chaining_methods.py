class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        
        return self

    # this method decrease the user's balance by the amount specified
    def make_withdrawl(self, amount): 
        self.account_balance -= amount
        
        return self

    # this method print the user's name and account balance to the terminal
    def display_user_balance(self): # eg. "User: Guido van Rossum, Balance: $150
        print(f"User: {self.name}, Balance: ${self.account_balance}")

        return self

    # Bonus - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)

        print(f"User: {self.name}, Balance: ${self.account_balance}")
        print(f"User: {other_user.name}, Balance: ${other_user.account_balance}")

        return self


# Create 3 instances of the User class
deidre = User("Deidre La Couse", "DeLaCouse@airs.com")
makeda = User("Makeda de Lioncourt", "DeLionMaker@airs.com")
olivia = User("Olivia de La Pieza", "OlaPieza@airs.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance

# print("Begining Balance:")
# deidre.display_user_balance()

deidre.make_deposit(70).make_deposit(100).make_deposit(67).make_withdrawl(45).display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance

# print("Begining Balance:")
# makeda.display_user_balance()

makeda.make_deposit(75).make_deposit(50).make_withdrawl(45).make_withdrawl(45).display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance

# print("Begining Balance:")
# olivia.display_user_balance()

olivia.make_deposit(1000).make_withdrawl(25).make_withdrawl(35).make_withdrawl(45).display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

# print("Deidre's Begining Balance:")
# deidre.display_user_balance()

# print("Olivia's Begining Balance:")
# olivia.display_user_balance()

deidre.transfer_money(olivia, 50)