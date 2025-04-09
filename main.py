# Bank account simulation (Python OOP project)

class BankAccount:
    def __init__(self , owner , balance=0):
        self.owner = owner
        self.balance = balance
        
    def Deposit(self , amount):
        if amount > 0:
            self.balance += amount    
            return f"Deposited Amount : {amount} . New Balance : {self.balance}"
        else:
            return "Deposit Amount must be Positive."
            
    def Withdraw(self , amount):
        if self.balance > 0 :
            self.balance -= amount
            return f"Withdrawl Amount {amount} . New Balance : {self.balance}"
        else:
            return "Your Account Balance Is Not sufficient to Withdraw the Amount."   
    
    def CheckBalance(self):
        print(f"{self.owner}'s Balance is Rs {self.balance}")
        return self.balance    
    
    def Transfer(self , transfer_acc , amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Transfer Amount of Rs{amount} is succesfull to {transfer_acc}"
        else:
            return f"Your Account Does not have Sufficient Balance to transfer the Amount."


owner = input("Enter Your Name : ")
balance = int(input(("Enter Your Account Balance : ")))

a = BankAccount(owner , balance)

while True:
    print("w = Withdraw , d = Deposit , c = Check Balance , t = Transfer")
    choice = (input("Choose the Transaction Option (w/d/c/t) : "))


    if choice =="w":
        amount = int(input("Enter the Amount : "))
        print(a.Withdraw(amount))
     
    elif choice =="d":
        amount = int(input("Enter the Amount : "))
        print(a.Deposit(amount))
    
    elif choice =="c":
        print(a.CheckBalance())
  
    elif choice =="t":
        transfer_acc = input("Enter the Tranfer Account Owner Name : ")
        amount = int(input("Enter the Amount : "))
        print(a.Transfer(transfer_acc , amount))
        
    else:
        print("invalid Option. Choose correct Option (w/d/c/t) : ")     

    again = input("Do you want to perform another transaction? (yes/no): ")
    if again.lower() == "yes":
        continue  
    else:
        print("Thank you for banking with us!")
        break
          
         
    
    
    
    
      
            
             
