import os
mydir = os.getcwd()
#print(mydir)

f = open('portfolio.csv', 'rt')
headers = next(f).split(',')
print(headers)
for line in f:
    print(line, end=' ')
f.close()
