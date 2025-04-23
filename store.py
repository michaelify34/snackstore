from abc import ABC, abstractmethod

#Snacks
class Snack(ABC):
    def __init__(self, price):
        self.price = price

class MandN(Snack):
    def __init__(self):
        self.name = "M&N"

class Scootles(Snack):
    def __init__(self):
        self.name = "Scootles"
    
#Drinks
class Drink(ABC):
    def __init__(self, price):
        self.price = price

class MrPepper(Drink):
    def __init__(self):
        self.name = "MrPepper"

class Brite(Drink):
    def __init__(self):
        self.name = "Brite"