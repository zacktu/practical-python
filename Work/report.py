# report.py
#
# Exercise 2.4

import sys
import csv

def read_portfolio(filename):
    """
    Build the portfolio
    """

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print('Bad row:', row)
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

my_portfolio = read_portfolio(filename)

print('My Portfolio:')
for name, shares, price in my_portfolio:
    print(name, shares, price)

total = 0
for name, shares, price in my_portfolio:
    total += shares * price

print('Total value is :', total)
