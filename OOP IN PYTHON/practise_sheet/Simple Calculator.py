class Calculator():
    def __init__(self,n1,n2,user_operation): 
        self.user_operation = user_operation
        self.n1 = n1
        self.n2 = n2
        self.select_operation()
    
        
    def select_operation(self):
        match self.user_operation:
            case 1:
                self.addition()
            case 2:
                self.subtractin()
            case 3:
                self.multiplication()
            case 4:
                self.devision() 
            case _:
                print("Enter a valid Operation Number") 
        
    def addition(self):
        out = self.n1 + self.n2
        print(f"result :-\n{out}")
    def subtractin(self):
        out = self.n1 - self.n2
        print(f"result :-\n{out}")
    def multiplication(self):
        out = self.n1 * self.n2
        print(f"result :-\n{out}")
    def devision(self):
        out = self.n1 / self.n2
        print(f"result :-\n{out}")
      
while(True):
    print("Enter first number")
    n1 = int(input())
    print("Enter second number")
    n2 = int(input())
    print("Select Operation\n1.)Addition\n2.)Subtraction\n3.)Multiplication\n4.)Division\n5.)Exit") 
    user = int(input())
    user1 = Calculator(n1,n2,user) 

    if(user == 5):
        print("You Quit...")
        break

       
        
