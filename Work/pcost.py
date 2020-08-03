# pcost.py
#
# Exercise 3.17: From filenames to file-like objects
#
# Usage: python pcost.py portfoliofilename
#

import sys
import fileparse

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    fileobject = open(filename, 'rt')
    portfolio = fileparse.parse_csv(fileobject, select=['name', 'shares', 'price'],
                                   types=[str, int, float])
    rowno = 0
    total_cost = 0
    try:
        for stock in portfolio:
            rowno+= 1
            print(stock['name'], stock['shares'], stock['price'])
            total_cost += stock['shares'] * stock['price']
    except ValueError:
        print(f'Row {rowno}: Bad row: {stock}')

    return total_cost

def main(args):
    if len(args) != 2:
        filename = input('Enter a filename:')
    else:
        filename = args[1]

    # for testing with same file
    #filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('\nTotal cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
