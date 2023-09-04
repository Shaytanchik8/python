from random import randint
n = randint(1, 5000)
k = randint(500, 1000)
print(n)
print(k)
print(n//k)
while n>k:
    n = n - k
print(n)