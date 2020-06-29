# gzip.py

import gzip
import os

print('Working directory is ', os.getcwd())

with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')