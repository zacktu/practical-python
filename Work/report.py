# Computer gain and loss for portfolii report.py
#
# Exercise 3.17: From filenames to file-like objects
#
# Usage report.py portfoliocsvfile pricesfilecsvfile
#

import fileparse

def read_portfolio(filename):
    fileobject = open(filename, 'rt')
    return fileparse.parse_csv(fileobject, select=['name', 'shares', 'price'],
                               types=[str, int, float])

def read_prices(filename):
    fileobject = open(filename, 'rt')
    return dict(fileparse.parse_csv(fileobject, types=[str, float],
                                         has_headers=False))

def build_stocklist(current_prices, original_portfolio):
    stocklist = []
    for stock in original_portfolio:
        shares = stock['shares']
        original_price = stock['price']
        current_price = current_prices[stock['name']]
        gainloss = current_price - original_price
        stocklist.append([stock['name'], shares, current_price, gainloss])
    return stocklist

def print_report(stocklist):
    '''
    :format and print the stock report
    '''
    print('      Name     Shares      Price     Change')
    print('---------- ---------- ---------- ----------')
    for name, shares, price, change in stocklist:
        dollarprice = '$' + str(price)
        print(f'{name:>10s} {shares:>10d} {dollarprice:>10s}'
                    f'{change:>10.2f}')

def portfolio_report(portfolio_file, prices_file):
    original_portfolio = read_portfolio(portfolio_file)
    current_prices = read_prices(prices_file)
    stocklist = build_stocklist(current_prices, original_portfolio)
    print_report(stocklist)
    print("\nThat's all folks!")

def main(args):
    # for quick testing to avoid typing
    # current_prices_filename = 'Data/prices.csv'
    # original_holdings_filename = 'Data/portfolio.csv'

    if len(args) != 3:
        original_holdings_filename = input('Enter name of portfolio file:')
        current_prices_filename = \
                    input('Enter name of current stock prices file:')
    else:
        original_holdings_filename = args[1]
        current_prices_filename = args[2]
    portfolio_report(original_holdings_filename, current_prices_filename)

if __name__ == '__main__':
    import sys
    main(sys.argv)
