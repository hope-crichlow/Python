class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

    # this method decrease the user's balance by the amount specified
    def make_withdrawl(self, amount): 
        self.account_balance -= amount

    # this method print the user's name and account balance to the terminal
    def display_user_balance(self): # eg. "User: Guido van Rossum, Balance: $150
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    # Bonus 
    # have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        print(f"User: {other_user.name}, Balance: ${other_user.account_balance}")
  


# Create 3 instances of the User class
deidre = User("Deidre La Couse", "DeLaCouse@airs.com")
makeda = User("Makeda de Lioncourt", "DeLionMaker@airs.com")
olivia = User("Olivia de La Pieza", "OlaPieza@airs.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
print("starting balance: $", deidre.account_balance)
deidre.make_deposit(70)
deidre.make_deposit(100)
deidre.make_deposit(67)
deidre.make_withdrawl(45)
print("ending balance: $", deidre.account_balance)

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
print("starting balance: $", makeda.account_balance)
makeda.make_deposit(75)
makeda.make_deposit(50)
makeda.make_withdrawl(45)
makeda.make_withdrawl(45)
print("ending balance: $", makeda.account_balance)

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
print("starting balance: $", olivia.account_balance)
olivia.make_deposit(1000)
olivia.make_withdrawl(25)
olivia.make_withdrawl(35)
olivia.make_withdrawl(45)
print("ending balance: $", olivia.account_balance)

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
print("Deidre's starting balance: $", deidre.account_balance)
print("Olivia's starting balance: $", olivia.account_balance)
deidre.transfer_money(olivia, 50)