#
# ticker.py
#
# Exercise 6.12 Putting it all together
#
# Selects columns from a pipeline
#

import tableformat
from report import read_portfolio
from follow import follow
import csv

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])

def main(args):
    if len(args) < 3:
        # portfolo_filename = 'Data/portfolio.csv'
        # stocklog_filename = 'Data/stocklog.csv'
        raise SystemExit\
            ('Usage: %s portfoliofile stocklogfile [format]' % args[0])
    else:
        portfolio_filename = args[1]
        stocklog_filename = args[2]
        if len(args) == 4:
            fmt = args[3]
        else:
            fmt = 'txt'
    ticker(portfolio_filename, stocklog_filename, fmt)

if __name__ == '__main__':
    import sys
    main(sys.argv)
    

