class Number:
    def __init__(self,num,user_op):
        self.n = num
        self.op = user_op
        self.select_operation()
        
    def select_operation(self):
        match self.op:
            case 1 :
                self.check_e_o()
            case 2 :
                self.is_prime()
            case 3 :
                self.calculate_factorial()
            case 4 :
                self.exit()
            case _:
                print("Enter valid Operation Number.")
                
    def check_e_o(self):
        if(self.n % 2 == 0):
            print(f"{self.n} is even.")
        else:
            print(f"{self.n} is odd.")
        
    def is_prime(self):
        arr = []
        for i in range(1,self.n + 1):
            if(self.n % i == 0):
                arr.append(i)
        if(len(arr)>2):
            print(f"{self.n} is Not Prime.")
        else:
            print(f"{self.n} is Prime.")
    
    def calculate_factorial(self):
        fact = 1
        if(self.n == 0 or self.n == 1):
            print(f"Factorial of {self.n} is {fact}")
        else:
            for i in range(1,self.n + 1):
                fact = fact * i
            print(f"Factorial of {self.n} is {fact}")
    
    def exit(self):
        print("You Quit....\nThankyou for using Number System Program.")    
    
n = int(input("Enter any number"))
print("Select Operation\n1.)Check Even or Odd\n2.)Check if number is prime\n3.)Calculate Factorial\n4.)Exit")
user_operation = int(input())
user1 = Number(n,user_operation)

        