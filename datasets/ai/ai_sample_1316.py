class BankAccount: 
    def __init__(self, ownerName, initialBalance):
        self.ownerName = ownerName
        self.balance = initialBalance
  
    def deposit(self, amount): 
        self.balance += amount
        print('Deposit Successful! Now your total balance is {}'.format(self.balance)) 
  
    def withdraw(self, amount):
        if amount > self.balance: 
            print('Insufficient balance!') 
        else: 
            self.balance -= amount
            print('Withdrawal Successful! Now your total balance is {}'.format(self.balance)) 
            
account1 = BankAccount("John", 1000)
account1.deposit(500)
account1.withdraw(200)