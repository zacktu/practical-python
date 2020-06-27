# gzip.py

import gzip

with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')
