class Student_Management():
    student = {101:"Rachit",102:"Pushpendra",103:"Archit",104:"Ankush"}
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
                self.add_student()
            case 2:
                self.display_student()
            case 3:
                self.search() 
            case _:
                print("Enter a valid Operation Number") 
        
    def display_student(self):
        print(f"{'Rollno':<30}{'Name':<30}")
        for i in Student_Management.student:
            print(f"{i:<30}{Student_Management.student[i]:<30}")
    def add_student(self):
        rollno = int(input(("Enter rollno of student to be added")))
        name = (input(("Enter name of student to be added")))
        Student_Management.student[rollno] = name
        print(f"{name} added Successfully")
    def search(self):
        rollno = int(input(("Enter rollno of student to search")))
        name = Student_Management.student[rollno]
        print(f"{name} is name of the student whose rollno is {rollno}.")
        
print("Enter username")
username = input()
print("Enter password")
password = input()

      
while(True):
    print("Select Operation\n1.)Add Student\n2.)Display Student\n3.)Search for a student by roll no.\n4.)Exit") 
    user = int(input())

    if(user == 4):
        print("You Quit...\nThankyou for using Student Management System.\nHave a nice Day!")
        break
    user1 = Student_Management(username,password,user) 

       
        
