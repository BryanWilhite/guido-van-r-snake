p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

print('unpacking the c-language-neutral (crappy) way:')

fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

print(fname, lname, age, email)

print('\nunpacking the Python way:')

fname, lname, age, email = p

print(fname, lname, age, email)
