names = [
    'raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith',
    'charlie'
]

print('do not do this:')

s = names[0]
for name in names[1:]:
    s += ', ' + name
print(s)


print('\nuse `join()`:')

print(', '.join(names))