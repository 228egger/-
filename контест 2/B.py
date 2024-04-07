import queue

n, m = map(int, input().split())


priority = queue.PriorityQueue(maxsize=m+1)

for i in range(m):
    priority.put(-1)

for i in range(n):
    name, begin, end = input().split()
    name = str(name)
    begin = float(begin.replace(':', '.'))
    end = float(end.replace(':', '.'))
    if priority.queue[0] < begin:
        priority.get()
        priority.put(end)
        print(name)
    else:
        print("No")

