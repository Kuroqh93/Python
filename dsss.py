class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def wag_tail(self):
        print(f"{self.name} розумніші за котів")

    def make_sound(self):
        print(f"{self.name}: Гав-гав!")

class Cat(Animal):
    def sharpen_claws(self):
        print(f"{self.name} лінивий")

    def make_sound(self):
        print(f"{self.name}: Мяу-мяу")

dog = Dog("Бакс")
cat = Cat("Бабабуй")

print("шо робить собака:")
dog.make_sound()
dog.wag_tail()

print("\nШо робить кіт:")
cat.make_sound()
cat.sharpen_claws()