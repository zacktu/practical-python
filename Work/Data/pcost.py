# pcost.py

def portfolio_cost():
    with open('portfolio.csv', 'rt') as f:
        headers = next(f).split(',')
        total_price = 0.0
        for line in f:
            linelist = line.split(',')
            total_price += int(linelist[1]) * float(linelist[2])
        return total_price

cost = portfolio_cost()
print('Total cost = ', cost)