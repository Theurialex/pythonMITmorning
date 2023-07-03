class peaple:
    def __init__(self, name, age, gender):
        self.peaplename = name
        self.peapleage = age
        self.peaplegender = gender

    def display(self):
        print(self.peaplename, self.peapleage, self.peaplegender)


myobj = peaple("Eric", 35, "Male")
myobj1 = peaple("Makena", 25, "Female")
myobj2 = peaple("Allan", 45, "Male")
myobj3 = peaple("Ines", 40, "Female")
myobj.display()
myobj1.display()
myobj2.display()
myobj3.display()
