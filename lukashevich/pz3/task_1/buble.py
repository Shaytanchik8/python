import random
from random import randint
import time
N = 10000
def Buble_sor(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
random.seed(42)
arr = [randint(1,99) for item in range(N)]

print(arr)
start_time = time.time()
Buble_sor(arr)
end_time = time.time()
print(arr)

print(end_time-start_time)