# pcost.py
#
# Exercise 5.6 Simple properties
#
# Usage: python pcost.py portfoliofilename
#


import report
from stock import Stock

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    total_cost = sum(stock.cost for stock in portfolio)
    return total_cost

def main(args):
    if len(args) != 2:
        # filename = 'Data/portfolio.csv'
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    else:
        filename = args[1]

    total_cost = portfolio_cost(filename)
    print('Total cost:', total_cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
