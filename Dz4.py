class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("деякі тварини можуть говорити по тваринячи")

class Pet:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("Він грається")

class Cat(Animal, Pet):
    def __init__(self, name, breed):
        Animal.__init__(self, species="Коте")
        Pet.__init__(self, name=name)
        self.breed = breed

    def make_sound(self):
        print("Мяу-Мяу")

    def eat(self):
        print("їсть")

class Dog(Animal, Pet):
    def __init__(self, name, breed):
        Animal.__init__(self, species="Шабака")
        Pet.__init__(self, name=name)
        self.breed = breed

    def make_sound(self):
        print("Гав-Гав!")

    def wag_tail(self):
        print("Ну він типу Who let the dogs out?"
              "woof, woof, woof, woof")
cat = Cat(name="КусокШерсті", breed="ВеслоВвусі")
dog = Dog(name="Патісон", breed="БульБульТерєр")


print(f"{cat.name} то є {cat.breed} {cat.species}")
cat.make_sound()
cat.eat()
cat.play()

print(f"{dog.name} то є {dog.breed} {dog.species}")
dog.make_sound()
dog.wag_tail()
dog.play()
