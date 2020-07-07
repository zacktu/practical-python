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
                #print('nextrow = ', nextrow)
                current_prices.update(nextrow)
                #print('current_prices = ', current_prices)
            except IndexError:
                pass
        #print('current_prices = ', current_prices)
    return current_prices

def getoriginalportfolio(originalholdings):

    """
    Build the portfolio
    """

    print('Entering getoriginalportfolio with files:', originalholdings)

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
        #print ('Portfolio = ', portfolio)
        return portfolio

# for quick testing to avoid typing
currentholdingsfilename = 'Data/prices.csv'
originalholdingsfilename = 'Data/portfolio.csv'

current_prices = getcurrentprices(currentholdingsfilename)
print('CURRENT PRICES =', current_prices)
print('CURRENT PRICE OF IBM IS', current_prices['IBM'])

original_portfolio = getoriginalportfolio(originalholdingsfilename)
print('ORIGINAL PORTFOLIO =', original_portfolio)
for stock in original_portfolio:
    print('name', stock['name'], stock['shares'], stock['price'])
    print('current price is ', current_prices[stock['name']])

# # print('ORIGINAL PORTFOLIO')
# # for stock in original_portfolio:
# #     print(stock['name'], stock['shares'], stock['price'])
#
# print('CURRENT PORTFOLIO')
# for current_stock in original_portfolio:
#     print(current_stock['name'], current_stock['price'])

#name = 'AA'
#print(current_prices['AA'])

#print('Current price of AA is:', current_prices['AA'])

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = input('Enter a filename:')
#
# stock_prices = current_prices(filename)
# print('stock_prices = ', stock_prices)
# print('Price of MSFT is ', stock_prices['MSFT'])
# print('Price of BAC is ', stock_prices['BAC'])
# print('Price of MMM is ', stock_prices['MMM'])

print("\nThat's all folks!")


