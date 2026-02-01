from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_(Product("laptop", 4000.5, 10))
manager.add_(Product("Phone", 2500.5, 30))
manager.add_(Product("Tablet", 1000.6, 15))

print("Products from inventory are:")
manager.display_all()

manager.total_inventory_value()
