import sys
from bisect import bisect_right, bisect_left
        
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
    

def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in args) + end)


def write_array(array, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in array) + end)



input = sys.stdin.buffer.readline
n = read_int()

for _ in range(n):
    m = read_int()
    tmp = read_int_list()
    arr = sorted([(val, key) for key, val in enumerate(tmp)])
    count = 0
    for i in range(1, len(arr)):
        if arr[i - 1][1] > arr[i][1]:
            count += 1
    print(count)
