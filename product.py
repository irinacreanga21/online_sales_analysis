
class Product:
    def __init__(self, name:str,price:float, quantity:int):
        self.name = name
        self.price  = price
        self.quantity = quantity
        
    def display(self):
        print(f"{self.name} - price: {self.price:.2f}, quantity:{self.quantity}")
        
    def act_quantity(self, amount:int):
        if amount <0:
            raise ValueError("quantity must be >=0")
        if amount >self.quantity:
            raise ValueError("insufficient stock")
        self.quantity -= amount