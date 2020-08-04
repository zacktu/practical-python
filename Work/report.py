# Computer gain and loss for portfolii report.py
#
# Exercise 3.18: Fixing existing functions
#
# Usage report.py portfoliofile pricesfile
#

import fileparse

def read_portfolio(filename):
    with open(filename) as lines:
        return fileparse.parse_csv(lines,
                select=['name', 'shares', 'price'],
                types=[str, int, float])

def read_prices(filename):
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines,
                types=[str, float],
                has_headers=False))

def make_report_data(original_portfolio, current_prices):
    stocklist = []
    for stock in original_portfolio:
        current_price = current_prices[stock['name']]
        gainloss = current_price - stock['price']
        stocklist.append([stock['name'], stock['shares'],
                current_price, gainloss])
    return stocklist

def print_report(stocklist):
    '''
    :format and print the stock report
    '''
    headers = ('Name', 'Price', 'Stock', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for stock in stocklist:
        print('%10s %10d %10.2f %10.2f' % tuple(stock))

def portfolio_report(portfolio_file, prices_file):
    original_portfolio = read_portfolio(portfolio_file)
    current_prices = read_prices(prices_file)
    report = make_report_data(original_portfolio, current_prices)
    print_report(report)

def main(args):
    if len(args) != 3:
        # portfolo_filename = 'Data/portfolio.csv'
        # prices_filename = 'Data/prices.csv'
        raise SystemExit('Usage: %s portfoliofile pricefile' % args[0])
    else:
        portfolio_filename = args[1]
        prices_filename = args[2]

    portfolio_report(portfolio_filename, prices_filename)

if __name__ == '__main__':
    import sys
    main(sys.argv)
