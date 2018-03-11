"""
    The `sorted()` function has no crappy C++ equivalents:
"""

colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
    print(color)

print('\nsort descending:')

for color in sorted(colors, reverse=True):
    print(color)

"""
    When a custom sort order is required,
    crappy C++ qsort habits have emerged (the -1,1,0 convention):
"""

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print('\ncrappy C++ style with `cmp=`:')

try:
    print(sorted(colors, cmp=compare_length))
except:
    print('Python 3.x no longer supports `cmp=`.')

"""
    Use the `key` parameter of the `sorted()` function
    before resorting to qsort habits:
"""

print('\ncool Python style:')

print(sorted(colors, key=len))

"""
    LINQ of the .NET Framework:

    `IEnumerable<string>.OrderBy(color => color.Length)`

    is the equivalent to the use of `sorted()` here in Python.
"""