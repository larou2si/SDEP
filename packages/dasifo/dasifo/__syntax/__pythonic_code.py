
x = 1 if True else 0

## Display a Number with comma
num = 10_000_000  # _ don't affect the number, it helps to read properly the value
print(f'{num:,}')  # => 10,000,000


## use context manager to read a file
with open('text.txt', 'r') as f:
    file = f.read()
f.close() # !! don't forget to close the file directly

## iterate an array
names = ['karim', 'sofien']
heros = ['superman', 'spiderman']
ages = [100,90]
for index, name in enumerate(names, start=1):
    print(index, name)

for name, hero, age in zip(names, heros, ages):
    print(f'{name} is {hero} aged {age}')

## UNPACKING values from list
a, b, _, c, *_ , d = (1, 2, 3, 4, 5, 6, 7)
print(a)  # => 1
print(b)  # => 2
print(c)  # => 4
print(d)  # => 7

# search variables: LEGB
# local, Enclosing, Global, Built-in

x = 'global x'
def outer():
    x = 'outer x'

    def inner():
        nonlocal x # refer to outer x
        x = 'inner x'
        print(x)

    inner()
    print(x)
outer()
print(x)


# ------- START contextmanager ----------------
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()

with open_file('test.txt', 'w') as f:
    f.write('sample text')

print(f.closed) # -- True
# ------- END contextmanager ----------------