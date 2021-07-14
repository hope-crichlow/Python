class Ninja:
    # Ninja class with the specified ninja attributes.
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    def walk(self):  # walks the ninja's pet invoking the pet play() method
        self.pet.play()
        return self

    def feed(self):  # feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()
        return self

    def bathe(self):  # cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()
        return self


class Pet:
    # Pet class with the specified pet attributes.
    def __init__(self, name, type, tricks="enthusiasm for a treats"):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    # implement the following methods:
    def sleep(self):  # increases the pets energy by 25
        self.energy += 25
        return self

    def eat(self):  # increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        return self

    def play(self):  # increases the pet's health by 5
        self.health += 5

    def noise(self):  # prints out the pet's sound
        if self.type == "dog":
            print("woof")
        elif self.type == "cat":
            print("meow")
        else:
            print("pitter patter")
        return self


# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
chocolate = Pet("Chocolate", "chinchilla", "beg")
haila = Ninja("Haila", "Star", "carrots", "kibble", chocolate)
print(haila.pet.name)

# Have the Ninja feed, walk , and bathe their pet.
# print(chocolate.health, chocolate.energy)
haila.feed().walk().bathe()
# print(chocolate.health, chocolate.energy)

# NINJA BONUS: Use modules to separate out the classes into different files.
# SENSEI BONUS: Use Inheritance to create sub classes of pets.
