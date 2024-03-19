import unittest
from test_product import TestProduct
from test_cart import TestShoppingCart

if __name__ == '__main__':
    # Define test suites
    product_suite = unittest.TestLoader().loadTestsFromTestCase(TestProduct)
    cart_suite = unittest.TestLoader().loadTestsFromTestCase(TestShoppingCart)

    # Combine test suites into a single suite
    all_tests = unittest.TestSuite([product_suite, cart_suite])

    # Run the tests
    unittest.TextTestRunner().run(all_tests)
