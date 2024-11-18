
class Employee:
    def __init__(self, name,position):
        self.name = name
        self.position = position

    #displays employees details
    def get_details(self):
        return f" Your name is {self.name} and you occupy {self.position} position"

employee1 = Employee("Priscilla Duah","Backend developer")




#inheritance
class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department
        
    def get_details(self):
         
         return f"Your name is {self.name} and you occupy {self.position} position in the {self.department} department"

manager1 = Manager("James Adam","Web developer", "IT")
print(employee1.get_details())
print(manager1.get_details())