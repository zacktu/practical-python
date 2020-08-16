#
# Section 4.1 Classes
# Exercise 5.7: Properties and Setters
#
# stock.py -- a class to represent stocks
#

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, numtosell):
        self.shares -= numtosell
        return self.shares

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'

    def __str__(self):
        return f'{self.name}-{self.shares}-{self.price}'
