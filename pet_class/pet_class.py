class Pet:
    def __init__(self, name, animal_type, age):
        self.name = " "
        self.animal_type = " "
        self.age = 0

    # setter method
    def set_name(self, name):
        self.name = name

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    # getter method
    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def get_age(self):
        return self.age