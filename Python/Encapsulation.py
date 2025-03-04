class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        print("getting age")
        return self.__age

    @age.setter
    def age(self, new_age):
        print(settimg new age)
        self.__age



    def display_info(self):
        print(f"Name: {self.name}, Age: {self.get_age()}")

person = Person("Alice Johnson", 30)
person.display_info()
