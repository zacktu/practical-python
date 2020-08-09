#
# tableformat.py
#
# Section 4.2 Inheritance
#
# Exercise 4.6: Using Inheritance to Produce Different Output
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