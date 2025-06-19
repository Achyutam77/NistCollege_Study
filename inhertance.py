class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age 


    def speak(self):
        pass

class Living:
    isAlive=True
    
class Dog(Animal,Living):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age)  
        self.weight = weight
        self.breed = breed

my_dog = Dog("kalu",8,15,"Labrador")
print(my_dog.name) 
print(my_dog.age)
print(my_dog.weight)   
print(my_dog.breed)

print(my_dog.isAlive)

#_ is protected variable 
class Cat(Animal, Living):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow"

#__is private variable
class Lion(Animal, Living):
    def __init__(self, name, age, mane_length):
        super().__init__(name, age)
        self.__mane_length = mane_length  # private variable

    def speak(self):
        return "Roar"

    def get_mane_length(self):
        return self.__mane_length  # method to access private variable
    
#polymorphism
