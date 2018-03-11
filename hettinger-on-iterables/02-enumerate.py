"""
    We can use `for` and `range` to loop over a list,
    showing indices, using crappy C++ style:
"""

colors = ['red', 'green', 'blue', 'yellow']

print('\ncrappy C++ style:')

for i in range(len(colors)):
    print(i, '-->', colors[i])

"""
    Or we can just use the `enumerate` function:
"""

print('\ncool Python style:')

for i, color in enumerate(colors):
    print(i, '-->', colors[i])

"""
    LINQ of the .NET Framework:

    `IEnumerable<string>.Select((color, i) => $"{i} --> {color}")`

    is the equivalent of the use of `enumerate()` above in Python.
"""