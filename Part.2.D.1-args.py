def do_nothing():
    pass

do_nothing()

import keyword
keyword.kwlist
keyword.iskeyword('if')


def do_something():
    print('This is a hello message from do_something().')

do_something()


def do_something():
    print('This is a message from do_something().')

if not do_something():
    print('The return value from do_something() is None.')


def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if leap % 100 == 0 and leap % 400 != 0:
            leap = False
    return leap 

is_leap(7)
is_leap(12)
is_leap(100)
is_leap(400)


def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
_is_leap(300)


def fib_between(start, end):
    a, b = 0, 1
    while a < end:
        if a >= start:
            print(a, end=' ')
        a, b = b, a+b 

fib_between(100, 10000)


def fib_between(start, end):
    r = []
    a, b = 0, 1
    while a < end:
        if a >= start:
            a.append(r)
            a, b = b, a+b 
        return r 

fib_between(100, 10000)


def increase_one(n):
    n += 1
    return n 

n = 1
print(increase_one(n))
print(n)


def be_careful(a, b):
    a = 2
    b[0] = 'What?!'

a = 1
b = [1, 2, 3]
be_careful(a, b)
print(a, b)


def be_careful(a, b):
    a = 2
    b_copy = b.copy()
    b_copy[0] = 'What?!'

a = 1
b = [1, 2, 3]
be_careful(a, b)
print(a, b)