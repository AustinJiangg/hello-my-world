def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):

year_leap_loop = _is_leap
year_leap_loop 
year_leap_loop(400)

id(_is_leap)
id(year_leap_loop)

type(_is_leap)
type(year_leap_loop)


def add(x, y):
    return x + y 

add(3, 7)


add = lambda x, y: x + y 
add(4, 7)


def make_incrementor(n):
    return lambda x: x + n 

f = make_incrementor(43)
f(1)
f(2)


def make_incrementor(n):
    return lambda x: x + n 

f = make_incrementor(43)
f 
id(make_incrementor) 
id(f)


def double_it(n):
    return n * 2

a_list = [1, 2, 3, 4, 5]
b_list = list(map(double_it, a_list))
b_list 
c_list = list(map(lambda n: n * 2, a_list))
c_list 


phonebook = [{'name': 'john', 'phone': '9876'},  {'name':'mike', 'phone':4753}]
phonebook 
list(map(lambda x: x['name'], phonebook))
list(map(lambda x: x['phone'], phonebook))


a_list = [1, 2, 3]
b_list = [4, 5, 6]
list(map(lambda x, y: x * y, a_list, b_list))


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p: p[1])
pairs 