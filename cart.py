# shopping_cart.py
class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_cost(self):
        total = 0
        for product in self.products:
            total += product.total_cost()
        return total
