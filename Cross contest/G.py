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
 
 
 
n, m = read_pair()
ans = ['declined'] * (n + m)
priority = queue.PriorityQueue(maxsize=n + m + 1)
balance_ = 0
for i in range(n + m):
    num = read_int()
    if num > 0: 
        balance_ += num
        ans[i] ='resupplied'
    else:
        if balance_ - abs(num) >= 0:
            priority.put((num, i))
            balance_ -= abs(num)
        else:
            if priority.qsize() > 0:
                res = priority.get()
                if abs(num) <= abs(res[0]):
                    balance_ += abs(res[0])
                    priority.put((num, i))
                    balance_ -= abs(num)
                else:
                    priority.put(res)
                
while priority.qsize() > 0:
    res = priority.get()
    ans[res[1]] = "approved"


for val in ans:
    print(val)