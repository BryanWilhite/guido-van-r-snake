"""
    We can use `for` to loop backwards through a list
    using crappy C++ style:
"""

colors = ['red', 'green', 'blue', 'yellow']

print('\ncrappy C++ style:')

for i in range(len(colors) - 1, -1, -1):
    print(colors[i])

"""
    Or we can just use the `reversed` function:
"""

print('\ncool Python style:')

for color in reversed(colors):
    print(color)


"""
    LINQ of the .NET Framework:

    `IEnumerable.Reverse()`

    is the equivalent of `reversed()` in Python.
"""