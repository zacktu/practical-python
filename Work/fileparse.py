# fileparse.py
#
# Section 3.3 Error Checking
#
# Exercise 3.7 Picking a different column delimiter

# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=''):
    '''
    Parse a CSV file into a list of records
    '''
    try:
        with open(filename) as f:
            if delimiter == '':
                rows = csv.reader(f)
            else:
                rows = csv.reader(f, delimiter=delimiter)

            if not has_headers:
                print('NO HEADERS')
                records = []
                for row in rows:
                    if not row:    # Skip rows with no data
                        continue
                    if select:
                        raise RuntimeError("select argument requires column headers")
                    if types:
                        row = [func(val) for func, val in zip(types, row)]
                    records.append(row)
            else:
                print('HEADERS')
                # Read the file headers
                headers = next(rows)

                # If a column selector was given, find indices of the specified columns.
                # Also narrow the set of headers used for resulting dictionaries
                if select:
                    indices = [headers.index(colname) for colname in select]
                    headers = select
                else:
                    indices = []

                records = []
                for row in rows:
                    if not row:    # Skip rows with no data
                        continue
                    # Filter the row if specific columns were selected
                    if indices:
                        row = [row[index] for index in indices ]
                    if types:
                        row = [func(val) for func, val in zip(types, row)]

                    # Make a dictionary
                    record = dict(zip(headers, row))
                    records.append(record)

            return records
    except ValueError as e:
        print(e)
