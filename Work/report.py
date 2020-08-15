# report.py  Compute gain and loss for portfolio
#
# Exercise 4.8 Putting it all together.
#
# Usage report.py portfoliofile pricesfile
#

import fileparse
from stock import Stock
from tableformat import TableFormatter, create_formatter

def read_portfolio(filename):
    with open('Data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(
                lines,
                select=['name', 'shares', 'price'],
                types=[str, int, float])
        portfolio = [Stock(q['name'], q['shares'], q['price'])
                     for q in portdicts]
        return portfolio

def read_prices(filename):
    with open(filename) as lines:
        return dict(fileparse.parse_csv(
                lines,
                types=[str, float],
                has_headers=False))

def make_report_data(original_portfolio, current_prices):
    stocklist = []
    for stock in original_portfolio:
        current_price = current_prices[stock.name]
        gainloss = current_price - stock.price
        stocklist.append([stock.name, stock.shares,
                          current_price, gainloss])
    return stocklist

def print_report(stocklist, formatter):
    '''
    Print a formatted table from a list of (name, shares, price, change) tuples.
    Print format is specified by formatter.
    '''

    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in stocklist:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_file, prices_file, format):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report_data(portfolio, prices)
    formatter = create_formatter(format)
    print_report(report, formatter)

def main(args):
    if len(args) < 3:
        # portfolo_filename = 'Data/portfolio.csv'
        # prices_filename = 'Data/prices.csv'
        raise SystemExit\
            ('Usage: %s portfoliofile pricefile [format]' % args[0])
    else:
        portfolio_filename = args[1]
        prices_filename = args[2]
        if len(args) == 4:
            format = args[3]
        else:
            format = 'txt'

    portfolio_report(portfolio_filename, prices_filename, format)

if __name__ == '__main__':
    import sys
    main(sys.argv)
