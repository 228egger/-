import sys
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



n = read_int()
k = read_int()
arr = []
switch = read_int_list()
for _ in range(n):
    arr.append(read_array())

arr = sorted(arr, key = lambda x: [-int(x[k]) for k in switch])
for i in range(n):
    write(arr[i][0])