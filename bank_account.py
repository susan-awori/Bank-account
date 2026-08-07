class Account:
    """A class representing a bank account operations."""
    
    def __init__(self, account_number: str, account_holder: str, account_balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = float(account_balance)

    def deposit(self, amount: float) -> float:
        """Adds the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
            print(f"[Deposit Success] Added ${amount:.2f} to Account {self.account_number}.")
        else:
            print("[Deposit Error] Deposit amount must be greater than zero.")
        return self.account_balance

    def withdraw(self, amount: float) -> float:
        """Subtracts the specified amount from the balance if sufficient funds exist."""
        if amount <= 0:
            print("[Withdrawal Error] Withdrawal amount must be greater than zero.")
        elif self.account_balance >= amount:
            self.account_balance -= amount
            print(f"[Withdrawal Success] Withdrew ${amount:.2f} from Account {self.account_number}.")
        else:
            print(f"[Withdrawal Failed] Insufficient funds in Account {self.account_number}. Current Balance: ${self.account_balance:.2f}")
        return self.account_balance

    def check_balance(self) -> float:
        """Returns and prints the current account balance."""
        print(f"[Balance Check] Account: {self.account_number} | Holder: {self.account_holder} | Balance: ${self.account_balance:.2f}")
        return self.account_balance

if __name__ == "__main__":
    
    print("--- 1. Initializing 'my_account' ---")
    my_account = Account(account_number="ACC-001", account_holder="Susan A.O", account_balance=500.00)
    
    # Testing methods 
    my_account.check_balance()
    my_account.deposit(6000.50)
    my_account.withdraw(4509.00)
    
    # Attempting insufficient funds
    my_account.withdraw(10000.00)
    my_account.check_balance()

    print("\n--- 2. Testing Multiple Instances ---")
    
    # Creating additional instances
    account_two = Account(account_number="ACC-002", account_holder="Caren A.O", account_balance=8970.05)
    account_three = Account(account_number="ACC-003", account_holder="Mamu O.A", account_balance=680.00)

    # transactions
    account_two.check_balance()
    account_two.deposit(5000.00)
    account_two.withdraw(3000.25)

    print("\n")
 #Testing transaction on Mamu
    account_three.check_balance()
    account_three.withdraw(999.00)  # trigger insufficient funds warning
    account_three.withdraw(150.00)   # Should succeed
    account_three.check_balance()