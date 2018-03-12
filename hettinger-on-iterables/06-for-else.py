"""
    We can use `for` and `enumerate`
    to find a list item by index using crappy C++ style:
"""

colors = ['red', 'green', 'blue', 'yellow']

print('\ncrappy C++ style:')


def find_cpp_style(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i

print(find_cpp_style(colors, 'blue'))

"""
    Or we can the `for`-`else` construct:
"""

print('\ncool Python style:')


def find_py_style(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

print(find_py_style(colors, 'blue'))

"""
    Raymond Hettinger says that inside every `for` is an `if` and `goto`
    which makes the use of `else` with `for` kind of make sense.

    Raymond would prefer that instead of `for`-`else` we would have `for`-`nobreak`.
"""
