import sys
input = sys.stdin.buffer.readline
import random
random.seed('codeforces!!111!')


#For demo
#f = open("t0", "r")
#input = f.readline


def read_int():
    return int(input())


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


t = read_int()
for _ in range(t):
    n, x = read_array()
    n = int(n)
    x = int(x)
    arr = sorted(read_int_list())
    pointer = 0
    count = 0
    h = arr[pointer]
    h_prev =  arr[pointer]
    cur_sum = 0
    while pointer < len(arr) and cur_sum <= x:
        h = arr[pointer]
        cur_sum += count * (h - h_prev)
        count += 1
        pointer += 1
        h_prev = arr[pointer - 1]
    if cur_sum <= x:
        write(h + (x - cur_sum) // count)
    else:
        count -= 1
        write(h + (x - cur_sum) // count)
