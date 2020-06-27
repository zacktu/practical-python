# portfolio_cost.py

def portfolio_cost():
    f = open('portfolio.csv', 'rt')
    headers = next(f).split(',')
    total_price = 0.0
    for line in f:
        linelist = line.split(',')
        total_price += int(linelist[1]) * float(linelist[2])
    f.close()
    return total_price

print('about to invoke portfolio_cost function')
cost = portfolio_cost()
print('returned from portfolio_cost function')
print('Total cost = ', cost)