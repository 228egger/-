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


#sys.stdout.flush()
#ans = read_int()


n, m = read_int_list()
left_A = 1
left_B = 1
count = 0
cur_count = 0
while left_A <= n and left_B <= m:
    write(f'? {left_A} {left_B}')
    sys.stdout.flush()
    ans = read_str()
    if "YES" in ans:
        cur_count += 1
        count += 1
        left_A += 1
    else:
        count += cur_count
        left_B += 1
count += cur_count * (m - left_B)
write(f'! {count}')
