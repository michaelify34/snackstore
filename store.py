from abc import ABC, abstractmethod

#Snacks
class Snack(ABC):
    pass

class MandN(Snack):
    def __init__(self):
        self._name = "M&N"
        self._price = 1.50

    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price

class Scootles(Snack):
    def __init__(self):
        self._name = "Scootles"
        self._price = 1.50

    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price


#Drinks
class Drink(ABC):
    pass

class MrPepper(Drink):
    def __init__(self):
        self._name = "MrPepper"
        self._price = 2

    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price

class Brite(Drink):
    def __init__(self):
        self._name = "Brite"
        self._price = 2

    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price


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
        self._balance = 10
        self._items = []

    @property
    def get_balance(self):
        return (f"Balance: ${self._balance}")
    
    def buy_item(self, item):
        self._items.append(item)
        self._balance -= item.price




s = Stock()
u = User()
s.generate_stock()
print(u.get_balance)
for i, good in enumerate(s.goods):
    print(f"{good.name}, ${good.price}, id: {i}")