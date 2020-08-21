#
# ticker.py
#
# Exercise 6.12 Puttint it all together
#
# Selects columns from a pipeline
#


from report import read_portfolio
from report import portfolio_report
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

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

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

    portfolio = read_portfolio(portfolio_filename)
    rows = parse_stock_data(follow(prices_filename))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        lst = []
        for i in row:
            lst.append(row[i])
        tple = tuple(lst)
        print(tple)


if __name__ == '__main__':
    import sys
    main(sys.argv)
    

