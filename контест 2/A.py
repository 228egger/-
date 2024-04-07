import queue

n, m = map(int, input().split())
ans = [0] * n


line = []
for _ in range(m):
    l, r = map(int, input().split())
    line.append([l, r])

cur = 0
priority = queue.PriorityQueue(maxsize=m + 1)
line.sort()
for i in range(1, n + 1):
    while cur < m and line[cur][0] == i:
        priority.put(line[cur][1], line[cur])
        cur += 1
    while not(priority.empty()) and priority.queue[0] < i:
        item = priority.get()
    ans[i - 1] = priority.qsize()
    



print(*ans)