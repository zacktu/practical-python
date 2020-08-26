#
# test_stock.py
#
# Exercise 8.1: Writing Unit Tests
#
# Use assertEqual and assertRaises from unittest to demonstrate simple testing
#

import unittest
import stock

class TestStock(unittest.TestCase):

    def test_bad_shares(self):
        s = stock.Stock('GM', 235, 32.56)
        self.assertEqual(s.name, 'GM')
        self.assertEqual(s.shares, 235)
        self.assertEqual(s.price, 32.56)
        self.assertEqual(s.cost, 7651.6)
        self.assertEqual(s.sell(35), 200)
        test_bad_shares(self)
        
    def test_bad_shares(self):
        s = stock.Stock('UAL', 100, 40.32)
        with self.assertRaises(TypeError):
            s.shares = 'IBM'

if __name__ == '__main__':
    unittest.main()
