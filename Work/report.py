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
                dict = {headers[0]:row[0], headers[1]:row[1], headers[2]: row[2]}
                portfolio.append(dict)
            except ValueError:
                print('Bad row:', row)
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

# for quick testing to avoid typing
#filename = 'Data/portfolio.csv'

my_portfolio = read_portfolio(filename)

print('\nMy Portfolio:')
total = 0
for stock in my_portfolio:
    print(stock['name'], stock['shares'], stock['price'])
    total += int(stock['shares']) * float(stock['price'])

print('\nTotal value is :', total)
