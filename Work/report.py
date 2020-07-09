#Computer gain and loss for portfolii report.py
#
# Exercise 2.11 Adding some headers

import csv

def getcurrentprices(currentportfolio):
    """
    Build the prices dictionary
    """

    current_prices = {}
    with open(currentportfolio, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                nextrow = {row[0]:row[1]}
                current_prices.update(nextrow)
            except IndexError:
                pass
    return current_prices

def getoriginalportfolio(originalholdings):

    """
    Build the portfolio
    """

    portfolio = []

    with open(originalholdings, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                dict = {headers[0]:row[0], headers[1]:row[1], headers[2]: row[2]}
                portfolio.append(dict)
            except ValueError:
                print('Bad row:', row)
        return portfolio

def make_report(current_prices, original_portfolio):
    stocklist = []
    for stock in original_portfolio:
        shares = int(stock['shares'])
        original_price = float(stock['price'])
        current_price = float(current_prices[stock['name']])
        gainloss = float(current_price - original_price)
        stocklist.append([stock['name'], shares, current_price, gainloss])
    return stocklist

# for quick testing to avoid typing
currentholdingsfilename = 'Data/prices.csv'
originalholdingsfilename = 'Data/portfolio.csv'

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = input('Enter a filename:')
#
# stock_prices = current_prices(filename)

current_prices = getcurrentprices(currentholdingsfilename)

original_portfolio = getoriginalportfolio(originalholdingsfilename)

stocklist = make_report(current_prices, original_portfolio)
print('      Name     Shares      Price     Change')
print('---------- ---------- ---------- ----------')
for name, shares, price, change in stocklist:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

'''
value = float(0.0)
for stock in original_portfolio:
    num_shares = float(stock['shares'])
    original_price = float(stock['price'])
    current_price = float(current_prices[stock['name']])
    gainloss = float(stock['shares']) * (current_price - original_price)
    value += gainloss
    print(stock['name'], stock['shares'], original_price, current_price, gainloss)
print('\nVALUE OF PORTFOLIO = ', value)
'''

print("\nThat's all folks!")


