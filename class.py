class fruits:
    def __init__(self,type,color,price):
        self.fruittype=type
        self.fruitcolor=color
        self.fruitprice=price
    def display(self):
        print(self.fruittype,self.fruitcolor,self.fruitprice)
myobj=fruits("banana","green",20)
myobj.display()