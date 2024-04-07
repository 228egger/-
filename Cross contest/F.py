import sys
from bisect import bisect_right, bisect_left
import queue
 
import sys
import random
random.seed('codeforces!!111!')
 
 
#For demo
#f = open("t0", "r")
#input = f.readline
 
 
def read_int():
    return int(input())
 
def read_str():
    return input()
 
def read_array(sep=None, maxsplit=-1):
    return input().split(sep, maxsplit)
 
    
def read_int_list(sep=None, maxsplit=-1):
    return [int(x) for x in input().split(sep, maxsplit)]
 
def read_pair():
    return map(int, input().split())
 
 
def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in args) + end)
 
 
def write_array(array, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in array) + end)
 
def get_med_stat(arr):
    n = len(arr)
    if len(arr) <= 5:
        arr = sorted(arr)
        if not(n % 2):
            return arr[n//2 - 1]
        else:
            return arr[n//2]
    arr_new = []
    i = 0
    while i + 5 < len(arr):
        arr_new.append(sorted(arr[i: i + 5])[2])
        i += 5
    n = len(arr[i:])
    arr = sorted(arr[i:])
    if not(n % 2):
        arr_new.append(arr[n//2 - 1])
    else:
        arr_new.append(arr[n//2])

    return get_med_stat(arr_new)

def partition(arr, m, left, right):
    pos = arr.index(m)
    arr[0], arr[pos] = arr[pos], arr[0]
    pivot = left
    for i in range(left + 1, right + 1):
        if arr[i] <= arr[left]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[left] = arr[left], arr[pivot]
    return pivot


def find_k_stat(arr, k):
    m = get_med_stat(arr)
    l = partition(arr, m, 0, len(arr) - 1)
    if k == l:
        return arr[l]
    elif k < l + 1:
        return find_k_stat(arr[:l], k)
    else:
        return find_k_stat(arr[l+1:], k - l - 1)

    


input = sys.stdin.buffer.readline





 
t = read_int()
for _ in range(t):
    n, k = read_pair()
    arr = read_int_list()
    write(find_k_stat(arr, k - 1))