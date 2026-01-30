class bankaccount: 
    #base class represents
    def __init__(self, accont_number, account_holder, balance=0):
        #attributes
        self.account_number = accont_number
        self.account_holder = account_holder
        self._balance = balance
    #method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Rs.{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
    #method to withdraw money
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")
    #method to check balance
    def get_balance(self):
        return self._balance
    #method to display account details
    def display_details(self):
        print("\nAccount Details")
        print("-----------------")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance        : Rs.{self._balance}")
#child class
class savingsaccount(bankaccount):
    #savings account with interest
    def __init__(self, accont_number, account_holder, balance=0, interest_rate=4):
        super().__init__(accont_number, account_holder, balance)
        self.interest_rate = interest_rate
    #method overriding
    def display_details(self):
        super().display_details()
        print(f"Interest Rate : {self.interest_rate}%")
#child class
class currentaccount(bankaccount):
    #with overdraft facility
    def __init__(self, accont_number, account_holder, balance=0, overdraft_limit=5000):
        super().__init__(accont_number, account_holder, balance)
        self.overdraft_limt = overdraft_limit
    #method overriding
    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limt:
            self._balance -= amount
            print(f"Rs.{amount} withdrawn using overdraft facility.")
        else:
            print("Overdraft limit exceeded.")
    def display_details(self):
        super().display_details()
        print(f"Overdraft Limit : Rs.{self.overdraft_limt}")
#real bank operations
if __name__ == "__main__":
    #creating  multiple objects
    savings = savingsaccount(1, "Darshana", 10000, 5)
    current = currentaccount(2, "Smit", 5000, 10000)
    #savings account operation
    savings.display_details()
    savings.deposit(2000)
    savings.withdraw(3000)
    print("Final Balance : ", savings.get_balance())
    #cuttent account operation
    current.display_details()
    current.withdraw(12000)
    current.deposit(5000)
    print("Final Balance : ", current.get_balance())