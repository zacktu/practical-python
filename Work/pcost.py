# pcost.py
#
# Exercise 3.14 Using more library imports
#
# Usage: python pcost.py filename
#

import sys
import fileparse

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    portfolio = fileparse.parse_csv(filename, select=['name', 'shares', 'price'],
                                   types=[str, int, float])
    rowno = 0
    total_cost = 0
    try:
        for stock in portfolio:
            rowno+= 1
            print(stock['name'], stock['shares'], stock['price'])
            total_cost += stock['shares'] * stock['price']
    except ValueError:
        print(f'Row {rowno}: Bad row: {row}')

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

# for testing with same file
#filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('\nTotal cost:', cost)
