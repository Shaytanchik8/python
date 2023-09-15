import random
from random import randint
import time
N = 15
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
arr = [randint(0,1) for item in range(N)]

print(arr)
start_time = time.time()
insertionsort(arr)
end_time = time.time()
print(arr)

print(end_time-start_time)

def source(arr):
    n = len(arr)
    k=0
    for i in range(0, n - 1):
        if arr[i] == 1:
            k+=1;
    return k

print(source(arr))