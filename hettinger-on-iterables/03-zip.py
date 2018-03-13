"""
    We can use `for`, `range` and `min`
    to loop over two lists using crappy C++ style:
"""

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

print('\ncrappy C++ style:')

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])

"""
    Or we can just use the `zip` function:
"""

print('\ncool Python style:')

for name, color in zip(names, colors):
    print(name, '-->', color)

"""
    LINQ of the .NET Framework:

    `IEnumerable<string>.Zip(IEnumerable<string>, (name, color) => $"{name} --> {color}")`

    is the equivalent of the use of `zip(<iterable>)` above in Python.

    Raymond Hettinger says that `zip` goes back 50 years to the original paper on Lisp.

    This decades-old history also implies that it is not taking advantage
    of modern caching in CPUs as `zip` uses a third list to combine the two original lists.

    It follows that Raymond Hettinger recommends the use of `izip`.

    However, the efficiency of `izip` is in the `zip` function of Python 3.x.
"""