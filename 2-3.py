# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def move(self):
        print(f"{self.name} moves around.")

# Derived class: Dog
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks: Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")

# Derived class: Cat
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows: Meow!")

    def climb(self):
        print(f"{self.name} climbs the tree gracefully.")

# Example usage
if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    dog.speak()     # Buddy barks
    dog.move()      # Buddy moves
    dog.fetch()     # Buddy fetches

    print("---")

    cat.speak()     # Whiskers meows
    cat.move()      # Whiskers moves
    cat.climb()     # Whiskers climbs
