from abc import ABC, abstractmethod

#Snacks
class Snack(ABC):
    pass

class MandN(Snack):
    def __init__(self):
        self.name = "M&N"

class Scootles(Snack):
    def __init__(self):
        self.name = "Scootles"


#Drinks
class Drink(ABC):
    pass

class MrPepper(Drink):
    def __init__(self):
        self.name = "MrPepper"

class Brite(Drink):
    def __init__(self):
        self.name = "Brite"


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

