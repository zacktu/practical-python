# fileparse.py
#
# Exercise 3.12 Using your library module
#
# Usage parse_csv(filename, select, types, has_headers, delimiter)

import csv

def parse_csv(filename, select=None, types=None,
                    has_headers=True, delimiter=''):
    '''
    Parse a CSV file into a list of records
    '''
    try:
        with open(filename) as f:
            if delimiter == '':
                rowno = 1
                rows = csv.reader(f)
            else:
                rowno = 1
                rows = csv.reader(f, delimiter=delimiter)

            if not has_headers:
                records = []
                for row in rows:
                    rowno+= 1
                    if not row:    # Skip rows with no data
                        continue
                    if select:
                        raise RuntimeError\
                                ("select argument requires column headers")
                    if types:
                        try:
                            row = [func(val) for func, val in zip(types,
                                                                  row)]
                            row = tuple(row)
                            #row = {func(val) for func, val in zip(types,
                            #                                      row)}
                            records.append(row)
                        except ValueError as e:
                            print('ERROR in row number', rowno, ': ', e)
            else:
                # Read the file headers
                rowno = 1
                headers = next(rows)

                # If a column selector was given, find indices
                #       of the specified columns.
                # Also narrow the set of headers used for
                #       resulting dictionaries
                if select:
                    indices = [headers.index(colname) for colname in select]
                    headers = select
                else:
                    indices = []

                records = []
                for row in rows:
                    rowno += 1
                    if not row:    # Skip rows with no data
                        continue
                    # Filter the row if specific columns were selected
                    if indices:
                        row = [row[index] for index in indices ]
                    if types:
                        try:
                            row = [func(val) for func, val in
                                   zip(types, row)]
                        except ValueError as e:
                            print('Error in row number', rowno, ': ', e)
                    # Make a dictionary
                    record = dict(zip(headers, row))
                    records.append(record)

            return records
    except RuntimeError as e:
        print('ERROR: ', e)

