import sys
from bisect import bisect_right
        
def read_int():
    return int(input())


input = sys.stdin.buffer.readline
n = read_int()

arr = [read_int()]
print(1)
for _ in range(n - 1):
    tmp = read_int()
    if tmp >= arr[-1]:
        arr.append(tmp)
    else:
        pos = bisect_right(arr, tmp, 0, len(arr) - 1)
        arr[pos] = tmp
    print(len(arr))

    

