class Animal:
    def __init__(self, name: str, species: str, age: int, adopted: bool):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__adopted = adopted
    
    def make_sound(self):
        return "This animal makes a sound"

class Dog(Animal):
    def new_animal(self, breed: str):
        return "Test"
    
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def new_animal(self, indoor_only: bool):
        return "Test"
    
    def make_sound(self):
        return "Meow!"