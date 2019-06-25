1.1 + 2.2


ord('a')
chr(100)

ord('和')
chr(3244)


'Simple is better than complex.'

"Simple is better than complex."

'''
Simple is better than complex.
Complex is better than complicated.
'''

"""
Simple is better than complex.
Complex is better than complicated.
"""


int('3')
float('3')
str(3.1415926)
int('3.1415926') # 报错
int(3.1415926) # 对的



age = input('Please tell me your age.')
if age < 18:
    print('I can't sell you drinking...)
else:
    print("Have a nice drink!")


age = int(input('''Please tell me your age:
an int number, e.g: 22
''')
if age < 18:
    print('I can not sell you drinks...')
else:
    print('Have a nice drink!')


'\\'

'\' # 报错

'He said, it\'s fine.'

"He said, it's fine."

"He said, it\'s fine."

s = "He said it\'s fine." # raw
print(s) # presentation


'Hey!' + ' ' + 'You!'

'Hey!' 'You!'

'Ha' * 7

'3.1415926' * 8

'o' in 'Hey, you!'


s = 'Python'
for char in s:
    print(s.index(char), char)

s = 'Python'
for i in range(len(s))
    print(s[i])

for i in s:
    print(i)

s = 'Python'
s[2]
s[2:]
s[2:5]
s[:5]
s[2:5:2]


ord('\n')
ord('\t')
ord('\r')
chr(65)
s = input('请照抄一遍这个数字：3.14: ')
int('3')
# int(s) 报错
float(s) * 9


'Now is better than never.'.upper()
_.lower()

s = 'Now is better than never.'
s.capitalize()
s.title()

s = 'Now is better than never.'
s.swapcase()
s.title()
s.title().swapcase()

s = '简单优于复杂。'
s.encode()


s = """Simple is better than complex.
Complex is better than complicated."""
s.lower().count('mp')
s.lower().count('mp', 10)
s.lower().count('mp', 10, 20)


print('Example of str.find():')
s = """Simple is better than complex.
Complex is better than complicated."""
s.lower().find('mpl')
s.lower().find('mpl', 10)
s.lower().find('mpl', 10, 20)
print()

print('Example of str.rfind():')
s = """Simple is better than complex.
Complex is better than complicated."""
s.lower().rfind('mpl')
s.lower().rfind('mpl', 10)
s.lower().rfind('mpl', 10, 20)

print('Example of str.index():')
s.lower().index('mpl')
s.lower().rindex('mpl')


s = """Simple is better than complex.
Complex is better than complicated."""
print('s.lower.startswith('S'):', s.lower.startswith('S'))
print('s.lower.startswith('b', 10), s.lower.startswith('b', 10))
print('s.lower.startswith('e', 11), s.lower.startswith('e', 11, 20))
print('s.lower.endswith('.'):', s.lower.endswith('.'))
print('s.lower.endswith('.', 10):', s.lower.endswith('.', 10))
print('s.lower.endswith('.', 10, 20):', s.lower.endswith('.', 10, 20))


s = """Simple is better than complex.
Complex is better than complicated."""
print('mpl' in s)


s = """Simple is better than complex.
Complex is better than complicated."""
print('s.lower().replace('mpl', [], 2): \n')
print(s.lower().replace('mpl', [], 2))


s = "Special\tcases\tare't\tspecial\tenougt\tto\tbreak\tthe\trules")
s.expandtabs()
s.expandtabs(2)


s = "\r \n Simple is better than complex. \n \t"
s 
s.strip()

s = "Simple is better than complex"
s 
s.strip('Six.p')
s.strip('Six.pmle')

s = "Simple is better than complex"
s 
s.lstrip('Six.p')
s.lstrip('Six.pmel')
s.rstrip('Six.p')
s.rstrip('Six.pmel')


s = """Name,Age,Location
John,18,New York
Mike,22,San Francisco
Janny,25,Miami
Sunny,21,Shanghai"""
s 
s.splitlines()
r = s.splitlines()[2]
r 
r.split()
r.split(sep=',')
r.split(',')
r.split(sep=',', maxsplit=1)
r.split(sep=',', maxsplit=0)
r.split(sep=',', maxsplit=-1)


s = ''
t = ['P', 'y', 't', 'h', 'o', 'n']
s.join(t)


s = 'Sparse is better than dense!'
s.title().center(60)
s.title().center(60, fillchar='*')
s.title().center(20)
s.title().rjust(60)
s.title().rjust(60, fillchar='*')


for i in range(1, 11):
    filename = str(i).zfill(3) + '.mp3'
    print(filename)


name = 'Alice'
age = 22
'{} is {} years olds'.format(name, age)
"Are you {}? -{{+}}".format(name)
'{} is a grown up? {}'.format(name, age >= 18)
name = 'Austin'
age = 21
f'{name} is {age} years old.'
f'{name} is a grown up? {age >= 18}'
name = "John"
age = 25
'{1} is {0} years old'.format(name, age)


print("'1234'.isalnum(): ', '1234'.isalnum())
print("'abcd'.isalpha(): ', 'abcd'.isalpha())
print("'草泥马'.isascii(): ', '草泥马'.isascii())
print("'0.123456789'.isdecimal(): ', '0.123456789'.isdecimal())
print("'0.123456789'.isdigit(): ', '0.123456789'.isdigit())
print("'0.123456789'.isnumeric(): ', '0.123456789'.isnumeric())
print("'Countine'.islower(): ', 'Counter'.islower())
print("'Simple is better than complex.'.isupper(): ', 'Simple is better than complex'.isupper())
print("'Simple Is Better Than Complex.'.istitle(): ', 'Simple Is Better Than Complex.'.istitle())
print("'\t'.isprintable(): ', '\t'.isprintable())
print("'\t'.isspace(): ', '\t'.isapace())
print("'for'.isidentifier(): ', 'for'.ifidentifier())