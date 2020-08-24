#
# typedproperty.py
#
# Define a class with property types for members
#

def typedproperty(name, expected_type):

    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)

if __name__ == '__main__':
    class Stock:
        name = String('name')
        shares = Integer('shares')
        price = Float('price')

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price  = price

    stock = Stock('GE', 125, 37.35)
    print(stock.name)
    print(stock.shares)
    print(stock.price)

    stock.price = 'MSFT'

