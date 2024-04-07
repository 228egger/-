import queue


n = int(input())

for _ in range(n):
    summa = 0
    t = int(input())
    cur_list = list(map(int, input().split()))
    priority = queue.PriorityQueue()
    for i in range(t):
        if cur_list[i] != 0:
            priority.put(-cur_list[i])
        elif not(priority.empty()) and cur_list[i] == 0:
            tmp = priority.get()
            summa -= tmp
        else:
            summa += 0
    print(summa)


    


