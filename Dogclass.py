class Dog:


    #constructor
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.thirst = 50
        self.obedience = 50
        self.energy = 50

    def stats(self):
        print("Dog stats:")
        print("Name: " + str(self.name))
        print("Hunger: " + str(self.hunger))
        print("Thirst: " + str(self.thirst))
        print("Obedience: " + str(self.obedience))
        print("Energy: " + str(self.energy), end = "\n\n")

    def fetch(self):
        if self.energy <= 0:
            print("Can't fetch. Too tired.")
        elif self.energy < 20:
            print("Look out! Dog is tired.")
            self.energy -= 5
            self.obedience += 5
            self.hunger += 5
            self.thirst += 10
        else:
            self.energy -= 5
            self.obedience += 5
            self.hunger += 5
            self.thirst += 10








dog1 = Dog('Fido')
dog1.stats()
dog1.fetch()
dog1.fetch()
dog1.fetch()
dog1.stats()
dog1.fetch()
dog1.fetch()
dog1.fetch()
dog1.stats()
dog1.fetch()
dog1.fetch()
dog1.fetch()
dog1.stats()
dog1.fetch()
dog1.fetch()
dog1.fetch()
dog1.stats()
