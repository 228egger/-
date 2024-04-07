import sys
import random
import queue

random.seed('codeforces!!111!')



#For demo
#f = open("t0", "r")
#input = f.readline


def read_int():
    return int(input())

def read_pair():
    return map(int, input().split())

def read_array(sep=None, maxsplit=-1):
    return input().split(sep, maxsplit)

    
def read_int_list(sep=None, maxsplit=-1):
    return [int(x) for x in input().split(sep, maxsplit)]



n, m = read_pair()
priority = queue.PriorityQueue(maxsize=n+1)

votes = read_int_list(sep = ' ')
counters = [0] * n
for i in range(n):
    priority.put((-votes[i], i))

while m > 0:
    party = priority.get()
    i = party[1]
    counters[i] += 1
    m -= 1
    priority.put((-votes[i]/(counters[i] + 1), i))


print(*counters)