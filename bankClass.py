class bankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
        self.transactions=[]
    def deposit(self,amount):
        if amount<0:
            print("The amount must be greater than 0.")
            return
        else:
           self.balance+=amount
           print(f"{amount} has been successfully deposited.")
           self.transactions.append({
                "Type": "Deposit",
                "Amount Deposited": amount,
                "Balance": self.balance
                })
           
    
    def withdraw(self,amount):
        if(amount<0):
            print("Enter a number greater than 0")
            return
        elif(amount<100):
            print(f"you cannot withdraw any amount less than 100")
            return
        elif(amount>self.balance):
            print(f"The amount you entered is greater than your account balance which is {self.balance}")
            return
        else:
            self.balance-=amount
            print(f"You have successfully withdrawn {amount}. \n Now your balance is {self.balance}")
            self.transactions.append({
                "Type": "Withdrawal",
                "Amount withdrawn": amount,
                "Balance": self.balance
            })
    def showBalance(self):
        print(f"Account Holder: {self.name} \n Account Balance: {self.balance}")
    
    def transactionHistory(self):
        if self.transactions:
            print("BELOW IS YOUR TRANSACTION HISTORY")
            for t in self.transactions:
                print("----")
                for key,value in t.items():
                    print(f"{key}: {value}")
                    
        else: 
            print("there has been no transaction.")
        
        
acc1=bankAccount("Faruk Adamu")
acc1.deposit(700000)
acc1.withdraw(50000)
acc1.showBalance()
acc1.transactionHistory()
        