class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")


student = Student("Alice Johnson", 20, "S12345")
teacher = Teacher("Bob Smith", 35, "Mathematics")

print("Student Information:")
student.display_info()
print()
print("Teacher Information:")
teacher.display_info()


###############################################################################################

class ElectronicDevice:
    def __init__(self, brand, model):
            self.brand = brand
            self.model = model

    def display_info(self):
            print(f"Brand: {self.brand}, Model: {self.model}")

class Laptop(ElectronicDevice):
    def __init__(self, brand, model, ram, storage):
            super().__init__(brand, model)
            self.ram = ram
            self.storage = storage

    def display_info(self):
            super().display_info()
            print(f"RAM: {self.ram}, Storage: {self.storage}")

class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, battery):
            super().__init__(brand, model)
            self.battery = battery
    def display_info(self):
            super().display_info()
            print(f"Battery: {self.battery} mAh")


laptop = Laptop("Dell", "XPS 13", "16GB", "512GB SSD")


smartphone = Smartphone("Apple", "iPhone 14", "3279")

print("Laptop Information:")
laptop.display_info()
print()
print("Smartphone Information:")
smartphone.display_info()