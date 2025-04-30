from abc import ABC, abstractmethod

#Snack classes
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


#Drink classes
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


#Handles store inventory
class Stock():
    def __init__(self):
        self.goods = []
        self.goods_list = [MandN(), Scootles(), MrPepper(), Brite()]
        
    #Create selection of snacks
    def generate_stock(self):
        for good in self.goods_list:
            self.goods.append(good)
        return self.goods

#Handles user interaction with interface
class User():
    def __init__(self):
        self._balance = 10
        self._items = []

    #Balance getter
    @property
    def get_balance(self):
        return (f"Balance: ${self._balance}")
    
    #Items getter
    @property
    def get_items(self):
        return self._items
    
    #Handles logic of user purchasing item
    def buy_item(self, item):
        if (self._balance - item.price) < 0:
            print("Insufficient funds")
            exit
        else:
            self._balance -= item.price
            self._items.append(item)

#Shell class for static method
class Menu():
    #Visualizes interface to allow user interactivity
    @staticmethod
    def store_run():
        (print("_____ Welcome to Michael's snack store! _____"),
    print("""
        To View Available Items: V 
   $$$ To Buy Item: input item code $$$
        To View Your Owned Items: E
         To View Your Balance: B
            !!! To Exit: Q !!!
            """))


#Runtime
if __name__ == "__main__":
    #Initialize necessary instances
    s = Stock()
    s.generate_stock()
    u = User()

    #While loop runs the visualization until the user exits
    loop = True
    while loop == True:
        Menu.store_run()
        user_selection = str(input("Selection: "))

            #User Exit
        if user_selection == "Q":
            print("Thank you for visiting Michael's snack store!")
            loop = False

            #View Available Items
        elif user_selection == "V":
            for i, good in enumerate(s.goods):
                print(f"{good.name}, ${good.price}, id: {i}")

            #Display Balance
        elif user_selection == "B":
            print(u.get_balance)
            
            #User Buy Item
        elif user_selection.isnumeric():
            u.buy_item(s.goods[int(user_selection)])

            #Display User's Items
        elif user_selection == "E":
            if len(u._items) == 0:
                print("You haven't bought anything yet!")
            else:
                itemlist = []
                for item in u.get_items:
                    itemlist.append(item.name)
                print(f"Items: {', '.join(_ for _ in itemlist)}")
            
        #Handles unexpected input
        else:
            print("Please make a valid selection.")