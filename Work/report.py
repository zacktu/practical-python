# Computer gain and loss for portfolii report.py
#
# Exercise 3.12 Using your library module
#
# Usage report.py portfoliocsvfile pricesfilecsvfile
#

import sys
import csv
import fileparse

def get_current_prices(current_portfolio):
    """
    Build the prices dictionary
    """

    current_prices = {}
    with open(current_portfolio, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                nextrow = {row[0]: row[1]}
                current_prices.update(nextrow)
            except IndexError:
                pass
    return current_prices


def get_original_portfolio(original_holdings):
    """
    Build the portfolio
    """

    portfolio = []

    with open(original_holdings, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                portfolio.append(record)
            except ValueError:
                print('Bad row:', row)

        # print('THats all for now!')
        # sys.exit()
        return portfolio


def build_stocklist(current_prices, original_portfolio):
    stocklist = []
    for stock in original_portfolio:
        shares = int(stock['shares'])
        original_price = float(stock['price'])
        current_price = float(current_prices[stock['name']])
        gainloss = float(current_price - original_price)
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


# for quick testing to avoid typing
# current_prices_filename = 'Data/prices.csv'
# original_holdings_filename = 'Data/portfolio.csv'

if len(sys.argv) == 3:
     original_holdings_filename = sys.argv[1]
     current_prices_filename = sys.argv[2]
else:
    original_holdings_filename = input('Enter name of portfolio file:')
    current_prices_filename = \
        input('Enter name of current stock prices file:')

#original_portfolio = get_original_portfolio(original_holdings_filename)
original_portfolio = fileparse.parse_csv(original_holdings_filename)
#current_prices = get_current_prices(current_prices_filename)
current_prices = fileparse.parse_csv(current_prices_filename, types=[str, float],
                                     has_headers=False)
current_prices_dict = dict(current_prices)
stocklist = build_stocklist(current_prices_dict, original_portfolio)
print_report(stocklist)
print("\nThat's all folks!")
