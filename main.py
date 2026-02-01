from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_(Product("laptop", 4000.5, 20))
manager.add_(Product("Phone", 2500.5, 50))
manager.add_(Product("Tablet", 1000.6, 15))

print("Products from inventory are:")

