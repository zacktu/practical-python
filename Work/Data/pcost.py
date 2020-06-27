# pcost.py

import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        total_price = 0.0
        for line in f:
            linelist = line.split(',')
            try:
                total_price += int(linelist[1]) * float(linelist[2])
            except ValueError:
                print ('Error in line: ', line)
        return total_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
    cost = portfolio_cost(filename)
else:
    cost = portfolio_cost('portfolio.csv')

print('Total cost = ', cost)