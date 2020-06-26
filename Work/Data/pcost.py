
f = open('portfolio.csv', 'rt')
headers = next(f).split(',')
print(headers)
total_price = 0.0
for line in f:
    linelist = line.split(',')
    print(linelist)
    total_price += int(linelist[1]) * float(linelist[2])
print("Total cost = ", total_price)
f.close()