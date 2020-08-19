#
# filematch.py
#
# Exercise 6.8 Setting up a simple pipeline
#
# Generator to return lines that match an argument
#

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line

if (__name__ == '__main__'):
    filematch(lines, substr)

