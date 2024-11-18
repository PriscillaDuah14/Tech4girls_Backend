class BankAccount:
    bank_name = "Tech4Girls Bank" 

    def __init__(self, account_holder):
        self.account_holder = account_holder  
        self.balance = 0 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}.\nNew balance: {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. \nNew balance: {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be a positive number.")

    @staticmethod
    def bank_policy():
        print("Welcome to Tech4Girls Bank. We prioritize your financial security.")

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

# Calling the class method
print("Bank Name:", BankAccount.get_bank_name())
    
# Demonstrating the functionality
account1 = BankAccount("Alice")
account1.deposit(100)  # Depositing money
account1.withdraw(50)   # Withdrawing money
account1.withdraw(100)  # Attempting to withdraw more than the balance

# Calling the static method
BankAccount.bank_policy()

