"""
    Raymond Hettinger wants to tell us that Python has `iter`
    to remedy the traditional approach to the sentinel-value (or control-break) pattern.

    Before he can do that he has to show us crappy way it was done in, say, C++.

    He shows us through the use of `open`, reading a text file:
"""

from functools import partial
import os

txt = f'{os.path.dirname(__file__)}/05-iter.txt'
size = 8

try:
    with open(txt) as f:

        print('crappy C++ style:')

        blocks = []
        while True:
            block = f.read(size)
            if block == '':
                break
            blocks.append(block)

        print(blocks)

    with open(txt) as f:

        print('\ncool Python style:')

        blocks = []
        for block in iter(partial(f.read, size), ''):
            blocks.append(block)

        print(blocks)

except IOError as err:
    print(err)

"""
    We see that `iter` depends on the use of `partial`
    such that `TextIOBase.Read()` can be a callable object
    without any parameters.
"""
