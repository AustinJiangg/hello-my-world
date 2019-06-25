def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n ** 0.5) + 1):
        if (n % m) == 0:
            return False
    else:
        return True 

for i in range(30, 110):
    if is_prime(i):
        print(i)


def func():
    pass
print(func())
print(print(func()))


abs(-3.1415926535)
int(abs(-3.1415926535))
float(int(abs(-3.1415926535)))


11 + 10 - 9 * 8 / 7 // 6 % 5
'3.14' + 3

type(3)
type(3.0)
type('3.0')
type(True)
type(range(10))
type([1, 2, 3])
type((1, 2, 3))
type({1, 2, 3})
type({'a':1, 'b':2, 'c':3})


True and False or not True


n = -95
n < 0 and (n + 1) % 2 == 0


'Awesome' + 'Python'
'Awesome' 'Python'
'Python, ' + 'Awesome! ' * 3
'o' in 'Awesome' and 'o' not in 'Python'


'a' < 'b'


'A' > 'a'
ord('A')
ord('a')


'PYTHON' > 'Python 3'


a_list = [1, 2, 3, 4, 5]
b_list = [1, 2, 3, 5]
c_lsit = ['ann', 'bob', 'cindy', 'dude', 'eric']
a_list > b_list
10 not in a_lsit 
'ann' in c_lsit


abs(-3.14159265)
divmod(11, 3)


import math
math.sin(5)


3.1415926.as_integer_ratio()


True or 'Python'


a = [1, 2, 3, 4, 5, 6, 7]
b = set(a)
c = list(b)
a 
b 
c 