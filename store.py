from abc import ABC, abstractmethod

#Snacks
class Snack(ABC):
    def __init__(self, price):
        self.price = price

    
#Drinks
class Drink(ABC):
    def __init__(self, price):
        self.price = price