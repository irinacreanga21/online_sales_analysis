class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_in_cart (self, item):
        self.cart_items.append(item)
    
    
    def display_cart(self):
        for i in self.cart_items:
            print(f"Products from cart are: {i.name} - quantity:{i.quantity}  - value {i.price*i.quantity}")
    
    
    def cart_value(self):
        total_cart_value = 0.0
        for item in self.cart_items:
            total_cart_value += item.price*item.quantity
        print(f"Total cart value is : {total_cart_value:.1f}")
        return total_cart_value
    
    

  
  
  
    
    
    