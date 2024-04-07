import sys

def read_int_list(sep=None, maxsplit=-1):
    return [int(x) for x in input().split(sep, maxsplit)]

def read_int():
    return int(input())

def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in args) + end)

def friends_leaving_order(n, p):
    leaving_order = []
    
    current_friend = 0
    for i in range(1, n+1):
        current_friend = (current_friend + p) % i
        leaving_order.insert(current_friend, i)
    
    return leaving_order

n, p = read_int_list()

order = friends_leaving_order(n, p)
write(*order)