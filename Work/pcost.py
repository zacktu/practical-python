# pcost.py
#
# Exercise 3.15 main() functions
#
# Usage: python pcost.py portfoliofile
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
