from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

manager.add_(Product("laptop", 4000.5, 20))
manager.add_(Product("Phone", 2500.5, 50))
manager.add_(Product("Tablet", 1000.6, 15))

print("Products from inventory are:")

manager.total_inventory_value()

cart = Cart()

cart.add_in_cart(Product("Laptop",4000.5, 1))
cart.add_in_cart(Product("Phone", 2500.5, 2))

cart.display_cart()
cart.cart_value()

