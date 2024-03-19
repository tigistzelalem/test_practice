# test_shopping_cart.py
import unittest
from product import Product
from cart import Cart

class TestShoppingCart(unittest.TestCase):

    def test_add_product(self):
        cart = Cart()
        self.assertEqual(0, 0)
        product = Product("Laptop", 1000, 2)
        cart.add_product(product)
        self.assertEqual(len(cart.products), 1)

    def test_total_cost(self):
        cart = Cart()
        product1 = Product("Laptop", 1000, 2)
        product2 = Product("Phone", 500, 3)
        cart.add_product(product1)
        cart.add_product(product2)
        self.assertEqual(cart.total_cost(), 3500)

if __name__ == '__main__':
    unittest.main()
