class Temperature():
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
                self.exit()
                
            case _:
                print("Enter a valid Operation Number") 
        
    def ctfk(self):
        c = int(input("Enter temperatur in Celsius"))
        f = ((9*c)/5) + 32
        k = c + 273.15
        print(f"Temperature in Fahrenheit is {f} and and kelvin is {k}")
    def ftck(self):
        f = int(input("Enter temperatur in Fahrenheit"))
        c = (f-32) * 5/9
        k = c + 273.15
        print(f"Temperature in Calsius is {c} and and kelvin is {k}")
    def ktcf(self):
        k = int(input("Enter temperatur in Kelvin"))
        c = k - 273.15
        f = ((9*c)/5) + 32
        print(f"Temperature in Celsius is {c} and and Fahrenheit is {f}")
    def exit(self):
        print("You Quit...\nThankyou for using Temperature Conversion Program")

      
while(True):
    print("Select Operation\n1.)Convert Celsius to Fahrenheit and Kelvin\n2.)Convert Fahrenheit to Celsius and Kelvin\n3.)Convert Kelvin to Celsius and Fahrenheit\n4.)Exit") 
    user = int(input())
    user1 = Temperature(user) 

    if(user == 5):
        print("You Quit...")
        break

       
        
