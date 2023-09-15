import random
from random import randint
import time
N = 10000
def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -  1
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
random.seed(42)
arr = [randint(1,99) for item in range(N)]

print(arr)
start_time = time.time()
insertionsort(arr)
end_time = time.time()
print(arr)

print(end_time-start_time)