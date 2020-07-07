# report.py
#
# Exercise 2.7 Computer gain and loss for portfolio

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
value = float(0.0)
for stock in original_portfolio:
    num_shares = float(stock['shares'])
    original_price = float(stock['price'])
    current_price = float(current_prices[stock['name']])
    value += float(stock['shares']) * \
             (float(current_prices[stock['name']]) -
              float(stock['price']))
print('value = ', value)

print("\nThat's all folks!")


