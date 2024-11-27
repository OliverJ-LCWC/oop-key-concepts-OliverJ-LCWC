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
    
    def animal_set_name(self, new_name):
        self.__name = new_name
    
    def animal_set_species(self, new_species):
        self.__species = new_species
    
    def animal_set_age(self, new_age):
        self.__age = new_age
    
    def animal_set_adopted(self, new_adopted):
        self.__adopted = new_adopted

    def make_sound(self):
        return "This animal makes a sound"
    
    

class Dog(Animal):
    def __init__(self, name: str, species: str, age: int, adopted: bool, breed: str):
        super().__init__(name, species, age, adopted)
        self.__breed = breed

    def animal_get_breed(self):
        return self.__breed
    
    def animal_set_name(self, new_breed):
        self.__breed = new_breed
    
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def __init__(self, name: str, species: str, age: int, adopted: bool, indoor_only: bool):
        super().__init__(name, species, age, adopted)
        self.__indoor_only = indoor_only

    def animal_get_breed(self):
        return self.__indoor_only
    
    def animal_set_name(self, new_indoor_only):
        self.__indoor_only = new_indoor_only

    def make_sound(self):
        return "Meow!"