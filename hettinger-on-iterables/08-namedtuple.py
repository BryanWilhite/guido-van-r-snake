"""
    Raymond Hettinger introduces the `namedtuple` in the context
    of `doctest` where the output of `doctest.testmod()` is a named tuple:
"""

import doctest

print(doctest.testmod())

"""
    We then replicate this output by defining our own named tuple:
"""

from collections import namedtuple

TestResults = namedtuple('TestResults', ['failed', 'attempted'])

print(TestResults(0, 4))
