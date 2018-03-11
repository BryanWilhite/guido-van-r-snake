"""
    Raymond Hettinger says that `for` should have been called `foreach`.

    This is because indices should almost always _never_ be used to do array lookups.

    The list of ten numbers below will be allocated entirely in memory:
"""

print('handmade list:')

for i in [0, 1, 2, 3, 4, 6, 7, 8, 9]:
    if (i % 2 == 0): print(i)

"""
    The `range` function was first developed to replicate the list above
    ---including the memory allocation.

    Then in order to save memory `xrange` was developed.

    Finally, `range` replaced `xrange` in order to do it right the first time:
"""

print('\nrange() function:')

for i in range(0, 9, 2):
    print(i)

"""
    Indices should almost always _never_ be used to do array lookups.

    This means that this C++ habit is not cool:
"""

colors = ['red', 'green', 'blue', 'yellow']

print('\ncrappy C++ style:')

for i in range(len(colors)):
    print(colors[i])

"""
    `for` in Python is just like `foreach` in C#:
"""

print('\ncool Python style:')

for color in colors:
    print(color)

"""
    LINQ of the .NET Framework:

    `Enumerable.Range()`

    is the equivalent of `range()` in Python.
"""