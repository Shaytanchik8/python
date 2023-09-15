import random
from random import randint
import time
N = 10000

random.seed(42)
arr = [randint(1,99) for _ in range(N)]

print(arr)
start_time = time.time()
sorted_list = sorted(arr)
end_time = time.time()
print(arr)

print(end_time-start_time)