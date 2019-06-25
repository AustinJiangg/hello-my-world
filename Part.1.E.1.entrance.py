import random
r = random.randrange(1, 10000)

if r % 2 == 0:
    print(r, "is even.")
else:
    print(r, "is odd.")


for i in range(10):
    if i % 2 != 0:
        print(i)


for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n/i) == 0:
            break
    else:
        print(n)


for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, int(n**0.5)+1):
        if (n % i) == 0:
            break
    else:
        print(n)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

for i in range(50, 90):
    if is_prime(i):
        print(i)


for i in range(20):
    if i % 2 != 0:
        print(i)
