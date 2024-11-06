# 5 ------------------------------------------------
# Create a class hierarchy for animals, starting with a base class Animal.
# Then, create subclasses like Mammal, Bird, and Fish.
# Add properties and methods to represent characteristics unique to each animal group.

class Animal:
    def __init__(self, name, size, ecosystem):
        self.size = size
        self.ecosystem = ecosystem
        self.name = name
    def eat(self):
        print(self.name, "is eating")
    def sleep(self):
        print(self.name, "is sleeping")

class Mammal(Animal):
    def __init__(self, name, size, ecosystem, type):
        super().__init__(name, size, ecosystem)
        self.type = type
    def walk(self):
        print(self.name, "is walking")
    def feed_kids_with_milk(self):
        print(self.name, "is feeding its children with milk")

class Bird(Animal):
    def __init__(self, name, size, ecosystem, isMigratory):
        super().__init__(name, size, ecosystem)
        self.isMigratory = isMigratory
    def fly(self):
        print(self.name, "is flying")

class Fish(Animal):
    def __init__(self, name, size, ecosystem, water_type):
        super().__init__(name, size, ecosystem)
        self.water_type = water_type # freshwater/saltwater
    def swim(self):
        print(self.name, "is swimming")

lioness = Mammal("Lioness", 130, "Savanna", "Carnivore")
kolibri = Bird("Kolibri", 3, "Jungle", False)
pike = Fish("Pike", 50, "Water", "Freshwater")

pike.eat()
pike.swim()
lioness.feed_kids_with_milk()
lioness.sleep()
kolibri.fly()
kolibri.sleep()

