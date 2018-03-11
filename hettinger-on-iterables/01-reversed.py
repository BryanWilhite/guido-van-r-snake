"""
    We can use `for` to loop backwards through a list
    using crappy C++ style:
"""

colors = ['red', 'green', 'blue', 'yellow']

print('\ncrappy C++ style:')

for i in range(len(colors) - 1, -1, -1):
    print(colors[i])

"""
    Or we can just use `reversed`:
"""

print('\ncool Python style:')

for color in reversed(colors):
    print(color)