import os
mydir = os.getcwd()
#print(mydir)

with open('portfolio.csv', 'rt') as f:
    for line in f:
        print (line, end = '')
