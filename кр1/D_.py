import sys
from collections import deque
 
input = sys.stdin.buffer.readline
 
def read_int_list(sep=None, maxsplit=-1):
    return [int(x) for x in input().split(sep, maxsplit)]
 
def read_int():
    return int(input())
 
def read_array(sep=None, maxsplit=-1):
    return input().split(sep, maxsplit)
 
def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in args) + end)
 
def friends_leaving_order(n, p):
    friends = deque(range(1, n+1))
    leaving_order = []
    index = 0
    while friends:
        index = (index + p - 1) % len(friends)
        friends.rotate(-index)
        print(friends, index)
        leaving_order.append(friends.popleft())
    
    return leaving_order
 
n, p = read_int_list()
 
order = friends_leaving_order(n, p)
write(*order)
