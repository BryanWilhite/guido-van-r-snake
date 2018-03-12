def fibonacci_basic(n):
    x = 0
    y = 1
    for i in range(n):
        print(i, '-->', x)
        t = y
        y = x + y
        x = t


print('basic function:')
print(fibonacci_basic(10))


def fibonacci_modern(n):
    x, y = 0, 1
    for i in range(n):
        print(i, '-->', x)
        x, y = y, x + y # no temp variables!


print('\nmodern function:')
print(fibonacci_modern(10))
