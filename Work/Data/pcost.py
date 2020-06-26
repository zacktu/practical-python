
f = open('portfolio.csv', 'rt')
headers = next(f).split(',')
print(headers)
total_price = 0.0
for line in f:
    #print(line, end=' ')
    linelist = line.split(',')
    #print(linelist)
    shares = linelist[1]
    price = linelist[2]
    purchase_price = int(shares) * float(price)
    print(shares, price, purchase_price)
    total_price += purchase_price
print("Total price = ", total_price)
f.close()