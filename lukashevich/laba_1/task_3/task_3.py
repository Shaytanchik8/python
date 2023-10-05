import random
def IsPositiveNumber(N):
    if N>0:
        return True
    else:
        return False
for i in range(5):
    r = random.randint(-10,10)
    print(r, "-", IsPositiveNumber(r))