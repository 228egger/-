import sys
input = sys.stdin.buffer.readline

def read_int():
    return int(input())
import queue
 
 

 
 
n, k = map(int, input().split())
q = queue.PriorityQueue(maxsize=k+1)


for i in range(1, n + 1):
    tmp = read_int()
    q.put(-tmp)
    if q.full():
        q.get()
    print(-q.queue[0])
