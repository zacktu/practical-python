import os
mydir = os.getcwd()
#print(mydir)

f = open('portfolio.csv', 'rt')
headers = next(f).split(',')
print(headers)
for line in f:
    row = line.split(',')
    print(row)
f.close()
