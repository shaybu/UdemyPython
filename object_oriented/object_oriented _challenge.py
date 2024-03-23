class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount Balance: ${self.balance}'

    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        print(f'added {deposit_amt} to the balance')

    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print(f'withdrawal accepted')
        else:
            print(f'You do not have money')


acct1 = Account('John Doe', 100)
print(acct1)
acct1.deposit(50)
print(acct1.balance)
acct1.withdrawal(20)
print(acct1.balance)
print(acct1.balance)
