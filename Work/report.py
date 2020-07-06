# report.py
#
# Exercise 2.7 Dictionaries as a container

import sys
import csv

def current_prices(filename):
    """
    Build the prices dictionary
    """

    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                next_row = {row[0]:row[1]}
                prices.update(next_row)
            except IndexError:
                pass

    return prices

# for quick testing to avoid typing
#filename = 'Data/prices.csv'

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

stock_prices = current_prices(filename)
print('stock_prices = ', stock_prices)
print('Price of MSFT is ', stock_prices['MSFT'])
print('Price of BAC is ', stock_prices['BAC'])
print('Price of MMM is ', stock_prices['MMM'])

print("\nThat's all folks!")


