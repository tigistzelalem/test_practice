# product.py
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        if self.price < 0 or self.quantity < 0:
            return 
        return self.price * self.quantity
