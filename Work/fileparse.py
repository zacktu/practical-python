# fileparse.py
#
# Exercise 8.2: Adding logging to a module
#
# Usage parse_csv(file-like object, select, types,
#       has_headers, delimiter, silence_errors)

import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(fileobject, select=None, types=None,
            has_headers=True, delimiter=',', silence_errors=False):

    '''
    Parse a CSV file into a list of records
    '''

    try:
        if select and not has_headers:
            raise RuntimeError('select requires column headers')
        rows = csv.reader(fileobject, delimiter=delimiter)

        #for row in rows:
            #print('AAAAAAAAA row = ', row)

        # Read file headers or set empty row
        headers = next(rows) if has_headers else []

        # If select specifies certain columns then apply to headers
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:         # Skip rows with no data
                continue

            # If specific column indices are selected. then select them
            if select:
                row = [row[index] for index in indices]

            # Apply type conversion to the row
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        log.warning("Row %d: Couldn't convert %s", rowno, row)
                        log.debug("Row %d: Reason %s", rowno, e)
                    continue

            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records

    except RuntimeError as e:
        print('ERROR: ', e)

