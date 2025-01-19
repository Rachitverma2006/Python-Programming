class Bank_Management():
    _balance = 10000
    def __init__(self,username,password,user_operation): 
        self.user_operation = user_operation
        self.username = username
        self.password = password
        self.validate_user()
    
    def validate_user(self):
        if(self.username == "Rachit" and self.password == "12345"):
            self.select_operation()
        else:
            print("Invalid User Credentials")  
    def select_operation(self):
        match self.user_operation:
            case 1:
                self.balance()
            case 2:
                self.add_money()
            case 3:
                self.withdraw() 
            case _:
                print("Enter a valid Operation Number") 
        
    def balance(self):
        print(f"Your Balane is {Bank_Management._balance}")
    def add_money(self):
        amount = int(input(("Enter amount to be added")))
        Bank_Management._balance += amount
        print(f"{amount} added Successfully")
    def withdraw(self):
        amount = int(input(("Enter amount to be withdraw")))
        Bank_Management._balance -= amount
        print(f"{amount} withdraw Successfully")
print("Welcome to Our Bank.")        
print("Enter username")
username = input()
print("Enter password")
password = input()

      
while(True):
    print("Select Operation\n1.)Check Balance\n2.)Add Money\n3.)Withdraw Money\n4.)Exit") 
    user_operation = int(input())

    if(user_operation == 4):
        print("You Quit...\nThankyou for visiting our bank.\nHave a nice Day!")
        break
    user1 = Bank_Management(username,password,user_operation) 

       
        
