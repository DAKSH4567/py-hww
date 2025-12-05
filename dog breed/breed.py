class Dog:
    species = "Canine"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def show(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Name:", self.name)
        print()


d1 = Dog("Labrador", "Buddy")
d2 = Dog("German Shepherd", "Rocky")

d1.show()
d2.show()
