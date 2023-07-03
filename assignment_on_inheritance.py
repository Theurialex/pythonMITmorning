class vehicles:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def enginetype(self):
        raise NotImplementedError("child class must implement this method")


class sportscar(vehicles):
    def enginetype(self):
        return "v8"


class sportscar(vehicles):
    def enginetype(self):
        return "v12"
class suv(vehicles):
    def enginetype(self):
        return "v12"
class suv(vehicles):
    def enginetype(self):
        def enginetype(self):
            return "v12"

    sportscar = sportscar("Toyota", "supra v8")
    print(sportscar.brand)
    print(sportscar.model)
    suv=suv("Chevrolet","suburban")
    print(suv.brand)
    print(suv.model)