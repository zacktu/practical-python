import os
mydir = os.getcwd()
#print(mydir)

f = open('Data/portfolio.csv')
headers = next(f).split(',')
print(headers)
for line in f:
    print(line, end=' ')
f.close()
