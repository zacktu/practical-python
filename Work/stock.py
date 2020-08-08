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

    def cost(self):
        return self.shares * self.price

    def sell(self, numtosell):
        self.shares -= numtosell
        return self.shares


