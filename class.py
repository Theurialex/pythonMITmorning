class fruits:
    def __init__(self,type,color,price,shape):
        self.fruittype=type
        self.fruitcolor=color
        self.fruitprice=price
        self.fruitshape=shape
    def display(self):
        print(self.fruittype,self.fruitcolor,self.fruitprice,self.fruitshape)
myobj=fruits("banana","green",20,"oval")
myobj.display()
myobj1=fruits("mango","yellow",30,"oval")
myobj1.display()
myobj2=fruits("orange","orange",15,"sphere")
myobj2.display()

#class called peaple with name age and gender
