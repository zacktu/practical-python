# pcost.py

import csv

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                print(record['name'], record['shares'], record['price'])
                numshares = int(record['shares'])
                shareprice = float(record['price'])
                total_cost += numshares * shareprice
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

    return total_cost

''' Use hardwired filename instead of prompt
import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')
'''

filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('\nTotal cost:', cost)
