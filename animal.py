class Animal:
    def __init__(self, name: str, species: str, age: int, adopted: bool):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__adopted = adopted

    def animal_get_name(self):
        return self.__name
    
    def animal_get_species(self):
        return self.__species
    
    def animal_get_age(self):
        return self.__age
    
    def animal_get_adopted(self):
        return self.__adopted
    
    def animal_set_name(self):
        return self.__name
    
    def animal_set_species(self):
        return self.__species
    
    def animal_set_age(self):
        return self.__age
    
    def animal_set_adopted(self):
        return self.__adopted

    def make_sound(self):
        return "This animal makes a sound"
    
    

class Dog(Animal):
    def new_animal(self, breed: str):
        return breed
    
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def new_animal(self, indoor_only: bool):
        return indoor_only
    
    def make_sound(self):
        return "Meow!"