names = [
    'raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith',
    'charlie'
]

print('this is way too slow:')

del names[0]
names.pop(0)
names.insert(0, 'mark')

print(names)

print('\nuse the `deque` container instead:')

from collections import deque

names = deque([
    'raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith',
    'charlie'
])

del names[0]
names.popleft()
names.appendleft('mark')

print(names)
