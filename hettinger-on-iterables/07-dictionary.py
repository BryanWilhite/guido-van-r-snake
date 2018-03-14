"""
    Raymond Hettinger says that mastering dictionaries is a _fundamental_ Python skill
    and he starts his Python classes with three days of work on dictionary relationships,
    counting, grouping and linking.

    The key-value relationship in a dictionary has been expressed in two ways:
"""

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

print('dictionary key-value immutable (default) relationship:')

for k in d:
    print(k)

print('\ndictionary key-value mutable relationship:')

for k in list(d.keys()):  # Python 3.x requires the use of list()
    if k.startswith('r'):
        del d[k]
print(d)

"""
    Explicitly printing out the relationship between keys and values
    has only one anti-pattern in Python 3.x:
"""

print('\ndictionary key-value relationship (anti-pattern):')

for k in d:
    print(k, '-->', d[k])  # causes re-hashing with every lookup

print('\ndictionary key-value relationship:')

for k, v in d.items():
    print(k, '-->', v)

"""
    The use of `items()` was replaced by `iteritems()` in Python 2.x
    because `items()` caused memory allocation(s) (tuple unpacking).

    In Python 3.x, `items()` is now the equivalent of `iteritems()`.

    In Python 3.x, we can generate a dictionary (`dict`) with `zip`,
    _linking_ two lists:
"""

print('\n`dict` and `zip`:')

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

print(dict(zip(names, colors)))

"""
    Raymond Hettinger shows us two ways to count with a dictionary.

    First, we see the beginners way:
"""

colors = ['red', 'green', 'red', 'blue', 'green', 'red']

print('\nbeginners counting:')

d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)

"""
    Then we discover the `get()` method of `dict`:
"""

print('\ncounting with `dict.get()`:')

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)

"""
    Then we get more modern with a subclass of `dict`,
    the `defaultdict`:
"""

from collections import defaultdict

print('\ncounting with `defaultdict`:')

d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)

"""
    We have our traditional way of grouping:
"""

names = [
    'raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith',
    'charlie'
]

print('\ntraditional grouping (by string length):')

d = {}
for name in names:
    key = len(name)  # grouping by string length
    if key not in d:
        d[key] = []
    d[key].append(name)
print(d)

"""
    Then, we have our traditional, Python-specific way of grouping
    with `dict.setdefault()`:
"""

print('\ntraditional, Python-specific way of grouping:')

d = {}
for name in names:
    key = len(name)  # grouping by string length
    d.setdefault(key, []).append(name)
print(d)

"""
    The modern way of grouping returns again to `defaultdict`:
"""

print('\nmodern way of grouping with `defaultdict`:')

d = defaultdict(list)
for name in names:
    key = len(name)  # grouping by string length
    d[key].append(name)
print(d)

"""
    Finally, we see that the linking dictionaries was traditionally
    involved with command-line argument parsing with `argparse`:
mm"""

import argparse
import os

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}

print('\ntraditional, memory-intensive way of linking dictionaries:')

d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

print(d)

print('\nmodern way of linking dictionaries:')

from collections import ChainMap

d = ChainMap(command_line_args, os.environ)

print(d)
