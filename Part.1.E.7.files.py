open('test-file.txt', 'w')


f = open('text-file.txt', 'w')
print(f.name)
f.close()


import os
f = open('test-file.txt', 'w')
print(f.name)
f.close()
if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted.')
else:
    print(f'{f.name} does not exist')


f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('test-file.txt', 'r')
s = f.read()
print(s)
f.close()


f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()
f = open('test-file.txt', 'r')
s = f.readline()
print(s)
s = f.readline()
print(s)
f.close()


f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()
f = open('test-file.txt', 'r')
s = f.readline().strip()
print(s)
s = f.readline().strip()
print(s)
f.close()


f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()
f = open('test-file.txt', 'r')
s = f.readlines()
print(s)
f.close()


f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()
f = open('test-file.txt', 'r')
for line in f.readlines():
    print(line)
f.close()


a_list = ['first line\n', 'second line\n', 'third line\n']
f = open('test-file.txt', 'w')
f.writelines(a_list)
f.close()
f = open('test-file.txt', 'r')
for line in f.readlines():
    print(line)
f.close()


import os

with open('test-file.txt', 'w') as f:
    f.write('first line\nsecond line\nthird line\n')

with open('test-file.txt', 'r') as f:
    for line in f.readlines():
        print(line)

if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted.')
else:
    print(f'{f.name} does not exist')


with open('word-alpha.txt', 'r') as file:
    for word in file.readlines():
        pass


ord('a')


word = 'knowledge'
sum = 0
for char in word:
    sum += ord(char) - 96
print(sum)


def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum 

sum_of_word('attitude')


def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(word) - 96
    return sum

with open('words-alpha.txt', 'r') as file:
    for word in file.readlines():
        if sum_of_word(word) == 100:
            print(word)



def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum 

with open('words-alpha.txt', 'r') as file:
    for word in file.readlines():
        if sum_of_word(word) == 100:
            print(word)
            for c in word:
                print(c, ord(c) - 96)
            break


def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum 

with open('words-alpha.txt', 'r') as file:
    for word in file.readlines():
        if sum_of_word(word.strip()) == 100:
            print(word)