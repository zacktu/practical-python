#
# Section 4.1 Classes
# Exercise 4.2 Adding some methods
#
# stock.py -- a class to represent stocks
#
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(s):
        return s.shares * s.price

    def sell(s, numtosell):
        s.shares -= numtosell
        return s.shares


