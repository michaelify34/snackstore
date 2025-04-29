from abc import ABC, abstractmethod

#Snacks
class Snack(ABC):
    pass

class MandN(Snack):
    def __init__(self):
        self._name = "M&N"
        self._price = 1.50

class Scootles(Snack):
    def __init__(self):
        self._name = "Scootles"
        self._price = 1.50


#Drinks
class Drink(ABC):
    pass

class MrPepper(Drink):
    def __init__(self):
        self._name = "MrPepper"
        self._price = 2

class Brite(Drink):
    def __init__(self):
        self._name = "Brite"
        self._price = 2


#Generate store inventory
class Stock():
    def __init__(self):
        self.goods = []
        self.goods_list = [MandN(), Scootles(), MrPepper(), Brite()]
        
    def generate_stock(self):
        for good in self.goods_list:
            for i in range(2):
                self.goods.append(good)
        return self.goods

class User():
    def __init__(self):
        pass



s = Stock()
s.generate_stock()
for good in s.goods:
    print(f"{good._name}, ${good._price}")