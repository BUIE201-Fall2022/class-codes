class Animal:
    def __init__(self) -> None:
        pass

    def talk(self):
        print("Animal doesn't know how to talk")

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def talk(self):
        print("Miyav")

class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def talk(self):
        print("Hav")

cat = Cat()
#cat.talk()

dog = Dog()
#dog.talk()

cat2 = Cat()
#cat.talk()

# polymorphism
my_pets = [cat, dog, cat2]
for pet in my_pets:
    pet.talk()