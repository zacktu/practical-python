# pcost.py

def portfolio_cost():
    with open('missing.csv', 'rt') as f:
        headers = next(f).split(',')
        total_price = 0.0
        for line in f:
            linelist = line.split(',')
            try:
                total_price += int(linelist[1]) * float(linelist[2])
            except ValueError:
                print ('Error in line: ', line)
        return total_price

cost = portfolio_cost()
print('Total cost = ', cost)