#
# tableformat.py
#
# Section 4.8 Putting it all together
#
# Exercise 4.11: Defining a custom exception
#

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''



class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr><th>'+'<th><th>'.join(headers)+'<th><tr>')

    def row(self, rowdata):
        print('<tr><td>'+'<td><td>'.join(rowdata)+'<td><tr>')

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError('Unknown table format %s' % name)
    return formatter

def print_table(objects, columns, formatter):
    formatter.headings(columns)
    for object in objects:
        rowdata = [str(getattr(object, colname)) for colname in columns]
        formatter.row(rowdata)
