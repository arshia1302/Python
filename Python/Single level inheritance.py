class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age > 18:
            print("Adult")
        else:
            print("Not adult")

class Employee(Person):

    def details(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

e1 = Employee("hari", 19)
e2 = Employee("zaid", 35)

e1.is_adult()
e2.is_adult()
print(e1.name)
print(e2.name)
print(e1.age)
print(e2.age)


#############################################################################

#Create a parent class Vehicle and pass attribute brand, model and take one method display info

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")

v1 = Vehicle("Toyota", "Fortuner")
v2 = Vehicle("Mahindra", "XUV500")

v1.display_info()
v2.display_info()
print(v1.brand)

#####################################################################################
#Create a parent class Vehicle and pass attribute brand, model and take one method display info
#create a child class Car and pass attribute year and same method display info

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year : {self.year}")


c1 = Car("Toyota", "Fortuner", 2002)
c2 = Car("Mahindra", "XUV500", 2007)

c1.display_info()
c2.display_info()
print(c1.brand)

##############################################################################################33

#Create a class Employee and pass argument name and position and take one method get_details
#Create a child class Manager and pass arguments department and method get_details

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"Name: {self.name}, Position : {self.position}"

class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def get_details(self):
        employee_details = super().get_details()
        return f"{employee_details}, Department : {self.department}"

e1 = Employee("Alice", "Engineer")
m1 = Manager("Bob", "Project Manager", "IT")

print(e1.get_details())
print(m1.get_details())
print(e1.name)



