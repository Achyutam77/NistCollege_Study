class Person:
    name="Ram"
    age=20
    address="Kathmandu"
    def get_height(self):
        return 5.5  

user=Person()
print(user.name)  # Ram
print(user.age)   # 20  
print(user.address)  # Kathmandu

print(user.get_height())  # 5.5

#constructor
class Person:
    def __init__(self, name, age, address): #defining constructor
        self.name = name
        self.age = age
        self.address = address

    def get_height(self):
        return 5.5
    def walk(self):
        print(f"{self.name} is walking")
    
user1 = Person("Ram", 20, "Kathmandu")  #creating object of class
user2 = Person("Shyam", 22, "Pokhara")  #creating another object of class
print(user1.name)  # Ram    
print(user2.name)  # Shyam

#methods
user1.walk()  # Ram is walking

