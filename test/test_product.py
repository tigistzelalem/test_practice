# test_product.py
import unittest
from product import Product

class TestProduct(unittest.TestCase):

    def test_total_cost(self):
        product = Product("Laptop", 1000, 2)
        self.assertEqual(product.total_cost(), 2000)

if __name__ == '__main__':
    unittest.main()
