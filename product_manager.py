
class ProductManager:
    def __init__ (self):
        self.products = []
        
    def add_(self, products):
        self.products.append(products)
        
    def display_all(self):
        for i in self.products:
            print (f"{i.name}-price:{i.price:.1f}, quantity:{i.quantity}")
            
            
    def remove_by_name(self, name:str):
        for c in self.products:
            if c.name == name:
                self.products.remove(c)
                break
            
    def total_inventory_value (self):
        total_value=0.0
        for i in self.products:
            total_value += i.price*i.quantity
        print(f"Total inventory value is: {total_value:.2f}")
        return total_value
            
        
        
        