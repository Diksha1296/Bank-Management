# Base class for BankAccount
class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        raise NotImplementedError("Withdraw method not implemented!")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

# Derived class for SavingsAccount
class SavingsAccount(BankAccount):
    MIN_BALANCE = 1000  # Minimum balance required in savings account

    def __init__(self, account_number, name, balance=0):
        super().__init__(account_number, name, balance)

    def withdraw(self, amount):
        if self.balance - amount < SavingsAccount.MIN_BALANCE:
            print("Cannot withdraw: Minimum balance requirement not met.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

# Derived class for CurrentAccount
class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = -5000  # Overdraft limit for current account

    def __init__(self, account_number, name, balance=0):
        super().__init__(account_number, name, balance)

    def withdraw(self, amount):
        if self.balance - amount < CurrentAccount.OVERDRAFT_LIMIT:
            print("Cannot withdraw: Overdraft limit exceeded.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

# Bank system class to manage the overall process
class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        print("\n--- Create Account ---")
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            print("Account number already exists. Please use a different account number.")
            return
        
        name = input("Enter account holder's name: ")
        account_type = input("Enter account type (savings/current): ").lower()
        
        if account_type == 'savings':
            self.accounts[account_number] = SavingsAccount(account_number, name)
        elif account_type == 'current':
            self.accounts[account_number] = CurrentAccount(account_number, name)
        else:
            print("Invalid account type. Account not created.")
            return
        
        print("Account created successfully!")

    def perform_deposit(self):
        print("\n--- Deposit Money ---")
        account_number = input("Enter account number: ")
        account = self.accounts.get(account_number)
        
        if not account:
            print("Account not found.")
            return
        
        try:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        except ValueError:
            print("Invalid amount entered.")

    def perform_withdrawal(self):
        print("\n--- Withdraw Money ---")
        account_number = input("Enter account number: ")
        account = self.accounts.get(account_number)
        
        if not account:
            print("Account not found.")
            return
        
        try:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        except ValueError:
            print("Invalid amount entered.")

    def check_balance(self):
        print("\n--- Check Balance ---")
        account_number = input("Enter account number: ")
        account = self.accounts.get(account_number)
        
        if not account:
            print("Account not found.")
            return
        
        account.check_balance()

    def transfer_money(self):
        print("\n--- Transfer Money ---")
        source_account_number = input("Enter source account number: ")
        destination_account_number = input("Enter destination account number: ")

        source_account = self.accounts.get(source_account_number)
        destination_account = self.accounts.get(destination_account_number)

        if not source_account:
            print("Source account not found.")
            return
        if not destination_account:
            print("Destination account not found.")
            return

        try:
            amount = float(input("Enter amount to transfer: "))
            if amount <= 0:
                print("Transfer amount must be positive.")
                return
            
            # Try withdrawing from the source account
            original_balance = source_account.balance
            source_account.withdraw(amount)

            # If the withdrawal was successful, deposit into the destination account
            if source_account.balance < original_balance:
                destination_account.deposit(amount)
                print(f"Transfer successful! {amount} transferred from {source_account_number} to {destination_account_number}")
            else:
                print("Transfer failed due to insufficient funds or restrictions.")
        except ValueError:
            print("Invalid amount entered.")

    def menu(self):
        while True:
            print("\n--- Bank Management System ---")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Transfer Money")
            print("6. Exit")
            
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.perform_deposit()
            elif choice == '3':
                self.perform_withdrawal()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                self.transfer_money()
            elif choice == '6':
                print("Exiting... Thank you for using the Bank Management System.")
                break
            else:
                print("Invalid choice. Please try again.")

# Main pro
bank_system = BankSystem()
bank_system.menu()
