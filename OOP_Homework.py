# 1. BankAccount
# Write a BankAccount class

# Attributes:

# owner
# balance (default 0)

# Methods:

# deposit(amount) → increases balance
# withdraw(amount) → decreases balance if enough money, otherwise prints “Insufficient funds.”
# Test:

# Create an account, deposit, withdraw, and print the balance.

class BankAccount:
    balance = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposits(self, amount = 50):
        self.balance += amount
        print("User deposited", amount)
        print(f"You now have: {self.balance}\n")

    def withdraw(self, amount = 100):
        self.balance -= amount
        print("You have withdrewn", amount)
        print(f"You now have: {self.balance}\n")

account1 = BankAccount("Vincent:",100)
account2 = BankAccount("Anna:",200)

print(account1.owner)
print(account1.balance)
print(account2.owner)
print(account2.balance)
print() # For spacing in the code

account1.deposits()# can i not add amount here for the deposits instead?
account1.withdraw()

account2.deposits()
account2.withdraw()

##########################################################################################################

# 2. Student
# Build a Student class

# Attributes:

# name
# grades (list)

# Methods:

# add_grade(grade) → adds a grade to the list
# average() → returns the average grade

# Test:

# Create a student, add grades, and print their average.

class Student:

    def __init__(self, name, grades):
        self.name = name
        
        if grades == None:
            self.grades = []
        else:
            self.grades = grades

    def add_grades(self, grades): # We append the grades in this method
        self.grades.append(grades)
        return (grades) # The None occured because we didnt let the method return anything, always return

    def average(self): # combine the student grades in this method with sum() and len()
        return sum(self.grades) / len(self.grades)
         

student1 = Student("Bryant",[50,60,70])
student2 = Student("James",[70,80,90])

# Here is info about Bryant:
print("Students name is",student1.name)
print(f"In the latest test Bryant got {student1.add_grades(99)}")
print("These are his grades",student1.grades)
print(f"And his average grade is {student1.average()}\n")

# Here is the info about James:
print("Students name is",student2.name)
print(f"In the latest test James got {student2.add_grades(100)}") #TODO: figure out why always returning None
print("These are his grades",student2.grades)
print(f"And his average grade is {student2.average()}\n")

##########################################################################################################

# 3. Company Hierarchy (Multi-Level Inheritance)
# Create a small company structure with three levels to explore inheritance and polymorphism.

# a) Employee (base class)

# Attributes:

# name
# skills (list)
# Methods:

# add_skill(skill) → adds a new skill to the list
# list_skills() → returns a string with all skills, e.g. "Python, SQL"

# b) Manager (child class of Employee)
# Additional Attribute:

# team (list of employee names)
# Methods:

# add_team_member(name) → adds a team member to the list
# Override list_skills() → include the manager’s team size in the returned string.

# c) Director (grandchild class of Manager)
# Additional Attribute:

# departments (list of department names)
# Methods:

# add_department(dep) → adds a department to the list
# overview() → returns a summary such as:

# "Director Alice manages 3 departments and a team of 10 people."
# Use super().__init__() in the constructors of Manager and Director to reuse code from the parent classes.

# Test:

# Create several Employee, Manager, and Director objects.
# Add skills, team members, and departments.
# Put them in a list and loop through it, calling list_skills() or overview() to show that each class behaves differently (polymorphism).

class Employee:

    def __init__(self, name, skills):
        self.name = name
        if skills is None:
            self.skills = [] # Weve now made skills into a list that will be unique for every person.
        else:
            self.skills = skills
        
    def add_skill(self, skill):
        self.skills.append(skill)
        (skill)
    
    def list_skills(self):
        return ",".join(self.skills)   


employee1 = Employee("Emma",["Java Script","Ruby","C++"])
employee2 = Employee("Durk", ["Java","Python","AI"])
employee3 = Employee("Bro", ["Java","Youtube","AI"])
employee4 = Employee("Jane", ["Pandas","Java","Java Script"])
employee5 = Employee("Goku", ["Strength","Martial Arts","Python"])
employee6 = Employee("Mary", ["HTMl","CSS","Java Script"])

print(f"{employee1.name} is an employee")
print(f"She has recently learned coding with Python")
employee1.add_skill("Python")
print(f"Her skills are now: {employee1.list_skills()}\n")

class Manager(Employee):

    def __init__(self, name, skills, team):
        super().__init__(name,skills)
        self.team = team
    
    def add_team_member(self, name):
        self.team.append(name)
    
    def list_skills(self):
        return "The team size is: "+str(len(self.team))+"\nTeam Members are: "+",".join(self.team)+"\nAnd the manager has these skills: "+",".join(self.skills)

chief = Manager("Bossman (Staff Manager)",["Super Power","ChatGPT"],[employee1.name, employee2.name, employee3.name, employee4.name])
print(chief.name)
print("Hes recently gained a new team member named Bruce")
chief.team.append("Bruce")
print(f"The team size is: {chief.list_skills()}")

chief2 = Manager("\nBosslady (Senior Manager)",["Karate","C#","C++"],[employee5.name,employee6.name])
print(chief2.name)
print (f"{chief2.list_skills()}")

class Director(Manager):

    def __init__(self, name, skills, team, departments):
        super().__init__(name,skills,team)
        self.departments = departments
    
    def add_department(self, dep):
        self.departments.append(dep)
    
    def overview(self):
        return "His team size is: "+str(len(self.team))+"\nTeam Members are: "+",".join(self.team)+"\nThe manager has these skills: "+",".join(self.skills)+"\nHe has recently gained control over the Production department"+"\nHe now controls these departments: "+",".join(self.departments)+"\n"
    
lord = Director("Champ (Director)",["Leading","Cooking","Chilling"],[chief.name,chief2.name],["Human resources","Finances"])
print("\nThe directors name is",lord.name)
lord.departments.append("Production")
print(lord.overview())

# Below is the loop that iterates through every role and person in the company

Company = [employee1,employee2,employee3,employee4,employee5,employee6,chief,chief2]

for person in Company:
    print(f"{person.name} {person.list_skills()}\n")

print(f"{lord.name} {lord.overview()}")