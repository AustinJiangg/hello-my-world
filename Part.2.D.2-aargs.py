def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')
    
say_hi()
say_hi('ann')
say_hi('mike', 'john', 'zeo')


def say_hi(*names):
	for name in names:
		print(f'Hi, {name}!')

names = ['ann', 'john', 'zeo']
say_hi(*names)


def say_hi(*names):
	for name in names:
		print(f'Hi, {name}!')

a_string = 'python'
say_hi(*a_string)
a_range = range(10)
say_hi(*a_range)
a_list = list(range(10, 0, -1))
say_hi(*a_list)
a_dictionary = {'ann':2321, 'mike':8712, 'joe':7610}
say_hi(*a_dictionary)


def say_hi(greeting, *names):
	for name in names:
		print(f'{greeting}, {name.capitalize()})

say_hi('Hello', 'ann', 'mike', 'joe')


def say_hi(greeting, *names, capitalized=False):
	for name in names:
		if capitalized:
			name = name.capitalize()
		print(f'{greeting}, {name}!')

say_hi('hello', 'mike', 'joe', 'zoe')
say_hi('hello', 'mike', 'joe', 'zoe', capitalized=True)


def say_hi(**names_greetings):
	for name, greeting in names_greetings.items():
		print(f'{name}, {greeting}!')

say_hi('mike'='Hi', 'ann'='Oh, my daring', 'joe'='Hello')


def say_hi(**names_greetings):
	for name, greeting in names_greetings.items():
		print(f'{name}, {greeting}!')

a_dictionary = {'mike'='Hi', 'an'='Oh, daring', 'joe':'Hello'}
say_hi(**a_dictionary)

say_hi(**{'mike'='Hi', 'ann'='Oh, daring', 'joe'='Hello'})

def say_hi_2(**names_greetings):
	for name in names_greetings:
		print(f'{names_greetings[name]}, {name}!')

say_hi_2(mike='hello', ann='oh, daring', joe='hi')


def say_hi(greeting, *names, capitalized=False):
	for name in names:
		if capitalized:
			name = name.capitalize()
		print(f'{greeting', {name}!')
	
say_hi('hi', 'mike', 'ann', 'joe')
say_hi('hi', 'mike', 'ann', 'joe', capitalized=True)


def say_hi(greeting='hello', *names, capitalized=False):
	for name in names:
		if capitalized:
			name = name.capitalize()
		print(f'{greeting}, {name}!')

say_hi('hi', 'mike', 'ann', 'joe')
say_hi('welcome', 'mike', 'ann', 'joe', capitalized=True)


def say_hi(*names, greeting='hi', capitalized=False):
	for name in names:
		if capitalized:
			name = name.capitalize.()
		print(f'{greeting}, {name}!')

say_hi('mike', 'ann', 'joe')
say_hi('mike', 'ann', 'joe', greeting='hello')