for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:
        print(n)


import random
r = random.randrange(1, 1000)

if r % 2 == 0:
    print(f'{f} is even.')


import random
r = random.randrange(1, 1000)

if r % 2 == 0:
    print(f'{r} is even')
else:
    print(f'{r} is odd')


import random
r = random.randrange(2, 13)

if r == 7:
    print('Draw!')
elif r < 7:
    print('Small!')
elif r > 7:
    print('Big!')


import random
r = randrange(0, 13)

if r == 7:
    print('Draw!')
elif r >= 2 and r < 7:
    print('Small!')
elif r > 7:
    print('Big!')
else:
    print('Not valid!')


for a in range(10):
    print(f'value of a: {a}')


range(10)
list(range(10))


list(range(1, 13))


for i in range(1, 10, 2):
    print(i)


list(range(0, -10, -1))


for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break 
    else:
        print(n)


for n in range(2, 100):
    if n == 2:
        print(2)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
    print(n)


for n in range(2, 100):
    if n == 2:
        print(2)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break 
        print(n)


def some_function():
    pass


for i in range(100):
    pass
    if i % 2 == 0:
        pass


n = 1000
a, b = 0, 1
while a < n:
    print(a, end=' ')
    a, b = b, a+b 
print()


from random import randrange
coin_user, coin_bot = 10, 10
rounds_of_game = 0

def bet（dict, wager):
    if dict = 7:
        return 0
    elif dict < 7:
        if wager = 's':
            return 1
        else:
            return -1
    elif dict > 7:
        if wager = 's':
            return -1
        else:
            return 1

while True:
    dict = range(2, 13)
    wager = input('What is your bet?')
    print(f'You: {coin_user}; Bot: {coin_bot}')
    
    if wager = 'q':
        break
    elif wager in 'bs':
        result = bet(dict, wager)
        coin_user += result
        coin_bot -= result
        rounds_of_game += 1
    if coin_user == 0:
        print(f'You've lost all, and game over!')
        break
    elif coin_bot == 0:
        print(f'The bot've list all, and game over!')
        break

