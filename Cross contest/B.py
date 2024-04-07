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




x = []
y = []
n = read_int()
for _ in range(n):
    x_y = read_int_list()
    x.append(x_y[0])
    y.append(x_y[1])

x = sorted(x)
y = sorted(y)
if not(n % 2):
    median_x = x[n//2 - 1]
    median_y = y[n//2 - 1]
else:
    median_x = x[n//2]
    median_y = y[n//2]
dist = 0
for i in range(n):
    dist += abs(x[i] - median_x) + abs(y[i] - median_y)

write(dist)