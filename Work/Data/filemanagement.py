import os
mydir = os.getcwd()
#print(mydir)

with open('portfolio.csv', 'rt') as f:
    data = f.read()

print (data)
