class Employee:
    def __init__(self, name, id, dept, salary):
        self.name = name
        self.id = id
        self.dept = dept
        self.salary = salary
        
    def display_info(self):
        print(f"{self.name:<15}{self.id:<15}{self.dept:<15}{self.salary:<15}")
        
    def update_info(self, name=None, id=None, salary=None):
        if name:
            self.name = name
        if id:
            self.id = id
        if salary:
            self.salary = salary
    
    def increment(self, increment):
        self.salary += (self.salary * increment) / 100
        print(f"Increment Successful of {self.name} by {increment}")
            
class Employee_management(Employee):
    def __init__(self):
        self.reg = {}
    
    def add_employee(self, id, name, dept, salary):
        if id in self.reg:
            print("Employee already exist")
        else:
            self.reg[id] = Employee(name, id, dept, salary)
            
    def delete_employee(self,id,name):
        if(id in self.reg):
            self.reg.pop(id)
            print(f"Employee {name} deleted.")
        else:
            print(f"Employee {name} not exist.")
        
    def display_all_employee(self):
        for emp in self.reg:
            self.reg[emp].display_info()
    
    def increment_by_id(self,id,perc):
        self.reg[id].increment(perc)
    
# Main


system = Employee_management()
while 1:
    
    
    print(f'''Available Choice\n
    1. Add Employee
    2. Update Employee Info
    3. Display All Employee
    4. Delete Employee By Id
    5. Salary Increment By Id
    6. Exit
          ''')
    choice = int(input("Enter the choice [1-6] "))
    if choice == 1:
        e_id = input('Enter the Employee Id')
        name = input('Enter the Employee Name')
        dept = input('Enter the Employee Department')
        salary = input('Enter the Employee Salary')
        
        system.add_employee(e_id,name,dept,salary)
    if choice == 2:
        e_id = input('Enter the Employee Id')
        name = input('Enter the Employee Name')
        salary = input('Enter the Employee Salary')
        system.update_info(name,e_id,salary)
        
    if choice == 3:
        print(f"{'Name':<15}{'ID':<15}{'Dept':<15}{'Salary':<15}")
        system.display_all_employee()
    
    if choice == 4:
        e_id = input('Enter the Employee Id')
        name = input('Enter the Employee Name')
        dept = input('Enter the Employee Department')
        salary = input('Enter the Employee Salary')
        
        system.delete_employee(e_id,name)
    
    if choice == 5:
        e_id = input('Enter the Employee Id')
        perc = input('Enter the Increment Percentage.')
        system.increment_by_id(e_id,perc)
        
        
        