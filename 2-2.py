class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a generic animal sound.")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says: Tweet!")

def animal_sound_demo(animals):
    for animal in animals:
        animal.make_sound()

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    bird = Bird("Tweety")

    animal_list = [dog, cat, bird]
    animal_sound_demo(animal_list)
