class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

        def speak(self):
            raise NotImplementedError("child class must empliment this method ")


class dog(animal):
    def speak(self):
        return "woof!"


class cat(animal):
    def speak(self):
        return "meows"


class guineapig(animal):
    def speak(self):
        return "groans"


# create an object
dog = dog("Tom", "brown")
print(dog.name)
print(dog.color)
print(dog.speak())
cat = cat("Bob", "black")
print(cat.name)
print(cat.color)
print(cat.speak())
guineapig = guineapig("Nester", "white")
print(guineapig.name)
print(guineapig.color)
print(guineapig.speak())
#crete a class called vihicles to have brand and model
