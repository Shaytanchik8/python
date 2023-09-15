import random
from random import randint
import time
N = 10000
def Sel_sort(arr):
    n = len(arr)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if arr[j] < arr[m]:
                m = j
        arr[j], arr[m] = arr[m], arr[j]
random.seed(42)
arr = [randint(1,99) for item in range(N)]

print(arr)
start_time = time.time()
Sel_sort(arr)
end_time = time.time()
print(arr)

print(end_time-start_time)